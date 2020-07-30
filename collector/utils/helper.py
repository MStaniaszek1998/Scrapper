# import standard
import codecs
import glob
import json
import logging
import os
from enum import Enum
from pathlib import Path
import urllib.parse
from typing import AnyStr, Optional, Tuple
from functools import lru_cache
# import third-party
import pandas as pd


class FileTypes(Enum):
    csv = 1
    html = 2


class Helper:
    SCRAPPING_MODE = None
    READ_TOKEN = False
    TOKEN = None

    @staticmethod
    def open_file(path: str) -> bytes:
        with codecs.open(path, 'r') as file:
            content = file.read()
        return content

    @staticmethod
    def save_file(save_path: str, content: AnyStr, stream_file=False,chunk_size=3000) -> None:
        """Generic function to save files"""
        if stream_file:
            with codecs.open(save_path, 'wb') as fd:
                for chunk in content.iter_content(chunk_size):
                    fd.write(chunk)
        else:
            with codecs.open(save_path, 'w') as file:
                file.write(content)

    @staticmethod
    def get_access_to_environment(env_name: str = 'DATA_LAKE') -> str:
        env_var = os.environ.get(env_name)
        if env_var is None:
            raise EnvironmentError(f'THERE IS NO {env_name} IN ENVIRONMENT ')
        else:
            return env_var

    @staticmethod
    def join_dir_base(dir, basename):
        return os.path.join(dir, basename)

    @staticmethod
    def create_folder(path: str) -> bool:
        """Creates a folder and returns a bool indicating if directory exists or not"""
        try:
            os.mkdir(path)
            return True
        except FileExistsError:
            return False

    @staticmethod
    def write_df_to_csv(path: str = None, content: pd.DataFrame = None):
        check_file_extension = path[-4:]
        extension = '.csv'
        if check_file_extension != extension:
            path = path + extension

        content.to_csv(path, index=False)

    @staticmethod
    def read_csv_to_df(path: str = None):
        dataframe = pd.read_csv(path)
        return dataframe


    @staticmethod
    def create_url(extended_path, base_path='https://icobench.com/'):
        url = urllib.parse.urljoin(base_path, extended_path)
        return url

