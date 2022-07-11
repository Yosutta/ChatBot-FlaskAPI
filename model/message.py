from lib.mysql_conn import mysqldb, mysqlerror

mysqlcursor = mysqldb.cursor()


class Message():
    def newMessage(message_id, conversation_id, message_text, formatted_time):
        try:
            query = 'INSERT INTO message (message_id, conversation_id, message_text, sent_time) VALUES(%s, %s, %s, %s)'
            value = (message_id, conversation_id, message_text, formatted_time)
            mysqlcursor.execute(query, value)
            mysqldb.commit()

        except mysqlerror as err:
            print(err)
            raise Exception('INTERNAL SERVER ERROR - DATABASE - TABLE MESSAGE')
