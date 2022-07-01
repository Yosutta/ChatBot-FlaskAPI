from lib.mysql_conn import mysqldb, mysqlerror

mysqlcursor = mysqldb.cursor()


class Conversation():
    def newConversation(conversation_id, formatted_time):
        try:
            query = 'INSERT INTO conversation (conversation_id, created_time) VALUES (%s, %s)'
            value = (conversation_id, formatted_time)
            mysqlcursor.execute(query, value)
            mysqldb.commit()

        except mysqlerror as err:
            print(err)
            raise Exception(
                'INTERNAL SERVER ERROR - DATABASE - TABLE CONVERSATION')
