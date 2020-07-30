from .helper import Helper
from .manager_plsql import ManagerPgSQL
import pandas as pd


def generate_path(path_extension: str = None):
    save_path = Helper.get_access_to_environment()
    folder_path = Helper.join_dir_base(save_path, path_extension)
    return folder_path





def get_save_path(path: str = 'DataLake/path'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            ## check if first part exist
            parent_folder = path.split('/')[0]
            parnet_folder_path = generate_path(path_extension=parent_folder)
            Helper.create_folder(parnet_folder_path)
            # Create later part
            folder_path = generate_path(path_extension=path)
            Helper.create_folder(folder_path)
            kwargs['save_point'] = folder_path
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


def connection_to_postgresql(database_name: str = 'Coinfirm'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            manager = ManagerPgSQL(database_name=database_name)

            with manager.get_connection() as conn:
                kwargs['conn'] = conn

                result = func(*args, **kwargs)
                return result

        return wrapper

    return decorator

@connection_to_postgresql(database_name='Coinfirm')
def get_dataframe(conn=None, get_query: str = None) -> pd.DataFrame:
    company_list = pd.read_sql_query(get_query, conn)
    return company_list


def get_ieos_list(crawler:str='Previous'):
    def decorator(func):
        def wrapper(*args, **kwargs):

            query = f"SELECT * FROM fn_get_ieos(crawler_name := '{crawler}')"
            dataframe = get_dataframe(get_query=query)

            kwargs['ieos_list'] = dataframe

            return func(*args, **kwargs)

        return wrapper

    return decorator
