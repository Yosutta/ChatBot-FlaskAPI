from http.client import HTTPException
from flask import Flask, make_response, request
from http import HTTPStatus
import uuid
from datetime import datetime, timedelta
import time
from flask_cors import cross_origin

from chatbot_script import createAnswer

# from model.message import Message as MessageModel
# from model.conversation import Conversation as ConversationModel

app = Flask(__name__)


@app.route("/chatbot", methods=['POST'])
@cross_origin()
def createMessage():
    try:
        conversation_id = request.json["conversation_id"]

        if not conversation_id:
            conversation_id = str(uuid.uuid4())
            time_now = datetime.now()
            formatted_time = time_now.strftime('%Y-%m-%d %H:%M:%S')
            # ConversationModel.newConversation(conversation_id, formatted_time)

        if(request.json['message']):
            message_id = str(uuid.uuid1())
            time_now = datetime.now()
            formatted_time = time_now.strftime('%Y-%m-%d %H:%M:%S')
            d = datetime.now() + timedelta(minutes=10)
            expire_time = int(time.mktime(d.timetuple())) * 1000

            # MessageModel.newMessage(
            # message_id, conversation_id, request.json['message'], formatted_time)
            answer = createAnswer(
                request.json['message']).replace("\n", "<br />\n")

            resp = make_response({"status": HTTPStatus.OK, "data": {
                                 'bot_answer': answer, 'conversation_id': conversation_id, "cookie_expire_time": expire_time}}, HTTPStatus.OK)

            return resp
        else:
            raise Exception("Missing user input")

    except Exception as err:
        error = str(err)
        print(error)
        resp = make_response(
            {"message": error, "error": "Internal server error"}, HTTPStatus.INTERNAL_SERVER_ERROR)
        return resp
