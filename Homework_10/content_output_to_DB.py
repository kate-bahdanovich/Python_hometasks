import pyodbc


class ContentToDB:
    # define class constructor to initialize db connection, cursor, and create DB tables for each data type
    def __init__(self, db_name='content.db'):
        self.db_name = db_name
        # define db connection
        self.connection = pyodbc.connect('DRIVER={SQLite3 ODBC Driver};'
                            'Direct=True;'
                            'Database=%s;'
                            'String Types= Unicode' % self.db_name, autocommit=True)
        # define cursor
        self.cursor = self.connection.cursor()
        # create tables if they not exist
        self.cursor.execute('CREATE TABLE IF NOT EXISTS News (news_text text, city text, news_date date)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Advert (adv_text text, adv_exp_date date, adv_date date)')
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS UserComment (comment_text text, comment_user_name text, comment_date date)')

    # define procedure for row inserting
    def insert_content(self, query):
        self.cursor.execute(query)

    # define destructor to close connection and cursor
    def __del__(self):
        self.cursor.close()
        self.connection.close()


# for testing  AND querying News,Advert,UserComment
if __name__ == '__main__':                                                      # for testing purpose
    x = ContentToDB(db_name="content.db")
    x.cursor.execute('select * from UserComment')
    result = x.cursor.fetchall()
    print(result)
