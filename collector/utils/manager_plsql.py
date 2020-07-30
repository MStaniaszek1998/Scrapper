# import standard

# import third-party
import psycopg2


# import own

class ManagerPgSQL:

    def __init__(self, database_name='Coinfirm'):
        self.connection = f"user=postgres password=postgres host=172.17.0.1 port=5432 " \
                          f"dbname={database_name} "

    def get_connection(self):
        return psycopg2.connect(self.connection)
