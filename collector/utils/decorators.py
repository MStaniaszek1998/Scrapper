from .helper import Helper
from .manager_plsql import ManagerPgSQL
import pandas as pd


def generate_path(path_extension: str = None):
    save_path = Helper.get_access_to_environment()
    folder_path = Helper.join_dir_base(save_path, path_extension)
    return folder_path


def get_ieos_list(crawler_name:str='Previouse'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            file_path = generate_path(path_extension=path)

            dataframe = pd.read_csv(file_path)

            kwargs['ieos_list'] = dataframe

            return func(*args, **kwargs)

        return wrapper

    return decorator


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
