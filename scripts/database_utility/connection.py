import pymysql


class MysqlConnect:
    """
        ----------------------------------------
        Class performs tasks on My SQL Database.
    """
    def __init__(self, db_creds, batch_size=50):
        self.username = db_creds.get('username')
        self.password = db_creds.get('password')
        self.host = db_creds.get('host')
        self.conn = None
        self.port = int(db_creds.get('port'))
        self.database = db_creds.get('database')
        self.batch_size = batch_size

    def connect(self):
        """
            --------------------------------------
            Establish connection between database.
        """
        try:
            self.conn = pymysql.connect(
                host=self.host,
                user=self.username,
                passwd=self.password,
                database=self.database)
            return self.conn
        except Exception as e:
            print("Connection Exception: ", str(e))

        return self.conn

    def cursor(self):
        """
            ---------------
            Returns cursor.
        """
        return self.conn.cursor()

    def close(self):
        """
            ----------------------
            Closes the connection.
        """
        self.conn.close()
        return True

    def execute_query(self, query):
        """
            ----------------------------------------------
            Executes the query and returns the table data.
        """
        try:
            cursor = self.cursor()
            cursor.execute(query)
            # obj = cursor.fetchall()
            obj = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
            return obj
        except Exception as e:
            print("Query Execution Exception: ", str(e))
            return []

    def execute_insert(self, query):
        """
            ---------------------------------------------------------
            Insert the values by executing  insert and committing it.
        """
        try:
            cursor = self.cursor()
            cursor.execute(query)
            self.conn.commit()
            return True
        except Exception as e:
            print("Insert Query Execution Exception: ", str(e))
        return False

