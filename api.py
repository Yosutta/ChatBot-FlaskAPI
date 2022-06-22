from http import HTTPStatus
from flask import Flask, make_response, request
from flask_restful import Resource, Api

from bot_script import createAnswer
from lib.mysql_conn import mysqldb

from model.message import Message as MessageModel
from model.conversation import Conversation as ConversationModel

import uuid
from datetime import datetime

app = Flask(__name__)
api = Api(app)

mysqlcursor = mysqldb.cursor()

# @app.route("/chatbot", methods=['POST'])
# def createConversation():
#     try:
#         conversation_id = str(uuid.uuid4())
#         time_now = datetime.now()
#         formatted_time = time_now.strftime('%Y-%m-%d %H:%M:%S')

#         query = 'INSERT INTO conversation (conversation_id, created_time) VALUES (%s, %s)'
#         value = (conversation_id, formatted_time)
#         mysqlcursor.execute(query, value)
#         mysqldb.commit()

#         resp = make_response(
#             {"status": HTTPStatus.OK, "data": {'conversation_id': conversation_id, "time": formatted_time}}, HTTPStatus.OK)
#         resp.set_cookie('conversation_id', conversation_id)
#         return resp

#     except:
#         resp = make_response(
#             {"message": "Internal server error"}, HTTPStatus.INTERNAL_SERVER_ERROR)
#         return resp


@app.route("/chatbot", methods=['POST'])
def createMessage():
    try:
        conversation_id = request.cookies.get('conversation_id')

        if not conversation_id:
            conversation_id = str(uuid.uuid4())
            time_now = datetime.now()
            formatted_time = time_now.strftime('%Y-%m-%d %H:%M:%S')
            ConversationModel.newConversation(conversation_id, formatted_time)

        if(request.json['message'] and conversation_id):
            message_id = str(uuid.uuid1())
            time_now = datetime.now()
            formatted_time = time_now.strftime('%Y-%m-%d %H:%M:%S')
            MessageModel.newMessage(
                message_id, conversation_id, request.json['message'], formatted_time)
            answer = createAnswer(request.json['message'])
            resp = make_response({"status": HTTPStatus.OK, "data": {
                                 'bot_answer': answer, 'conversation_id': conversation_id}}, HTTPStatus.OK)
            resp.set_cookie('conversation_id', conversation_id)
            return resp
        else:
            raise Exception("Missing user input")

    except Exception as err:
        error = str(err)
        resp = make_response(
            {"message": error, "error": "Internal server error"}, HTTPStatus.INTERNAL_SERVER_ERROR)
        return resp


if __name__ == '__main__':
    app.run(debug=True)
