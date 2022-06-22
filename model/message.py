from lib.mysql_conn import mysqldb


class Message():
    def newMessage(message_id, conversation_id, message_text, formatted_time):
        try:
            mysqlcursor = mysqldb.cursor()

            query = 'INSERT INTO message (message_id, conversation_id, message_text, sent_time) VALUES(%s, %s, %s, %s)'
            value = (message_id, conversation_id, message_text, formatted_time)
            mysqlcursor.execute(query, value)
            mysqldb.commit()

        except:
            raise Exception('INTERNAL SERVER ERROR - DATBASE')
