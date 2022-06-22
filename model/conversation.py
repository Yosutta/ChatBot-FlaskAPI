from lib.mysql_conn import mysqldb

mysqlcursor = mysqldb.cursor()


class Conversation():
    def newConversation(conversation_id, formatted_time):
        try:
            query = 'INSERT INTO conversation (conversation_id, created_time) VALUES (%s, %s)'
            value = (conversation_id, formatted_time)
            mysqlcursor.execute(query, value)
            mysqldb.commit()
            
        except:
            raise Exception('INTERNAL SERVER ERROR - DATBASE')
