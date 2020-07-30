from tqdm import tqdm
from .helper import Helper
from .pgsql_executor import PLSQLExecutor
class Inserter:

    def __init__(self,csv_to_insert:str=None,col_url:str=None):
        self.df = Helper.read_csv_to_df(path=csv_to_insert)
        self.insert_col = col_url

    def insert_url_to_database(self,crawler_name):
        for _,row in tqdm(self.df.iterrows()):
            url = row[self.insert_col]
            PLSQLExecutor.insert_new_urls(url=url, crawler_name=crawler_name)
