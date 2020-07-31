from .decorators import connection_to_postgresql


class PLSQLExecutor:
    @staticmethod
    @connection_to_postgresql(database_name='Coinfirm')
    def insert_new_urls(conn, url: str = None, crawler_name: str = None, project_name: str = None):
        cursor = conn.cursor()
        query = "CALL insert_new_urls(url:= %s, crawler := %s,project_name := %s )"
        cursor.execute(query, (url, crawler_name, project_name))
        cursor.close()

    @staticmethod
    @connection_to_postgresql(database_name='Coinfirm')
    def update_urls(conn, url: str = None, status_code: int = 0, scrape_time_a='2020-07-30'):
        cursor = conn.cursor()
        query = "call update_urls(url_a := %s,status_code_a := %s,scrape_time_a := %s);"
        cursor.execute(query, (url, status_code, scrape_time_a))
        cursor.close()

    @staticmethod
    @connection_to_postgresql(database_name='Coinfirm')
    def delete_rows_url(conn):
        cursor = conn.cursor()
        query = "CALL delete_all_rows();"
        cursor.execute(query)
        cursor.close()