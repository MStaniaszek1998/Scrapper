"""Base class for each parser which gives the access to common use functions"""
import glob
import os
from abc import abstractmethod, ABC
from datetime import datetime
# import standard
from typing import Optional, Tuple, AnyStr, Dict, Union

# import third-party
from bs4 import BeautifulSoup
import bs4

# import own
from utils import Helper, FileTypes


class ScrapperBase(ABC):
    def __init__(self, path_to_scrapped: str = None):
        self.config_path = path_to_scrapped
        self.scrapped_list_path = None

    @abstractmethod
    def parse_files(self):
        pass

    def find_in_soup(self, soup: BeautifulSoup = None, tag: str = None, attributes: Dict[str, str] =
    None, key: str = None, value_to_get: str = None, get_only_text: bool = True) -> Optional[str]:
        try:
            if get_only_text:
                element = soup.find(tag, attrs=attributes).text
                return element
            else:
                element = soup.find(tag, attrs=attributes).get(value_to_get)
                return element
        except:

            print("NO VALUE FOR %s", key)
            return None

    def _check_if_attr_exists(self, xpath: str, root, attribute: str,
                              return_all_join: bool = False) -> Optional[str]:
        """Checks if the attribute is available in the root of lxml parsed document"""
        try:
            main = root.xpath(xpath)

            if return_all_join:
                return "~".join(main)
            elif return_all_join == False:
                return main[0]
            else:
                return None
        except IndexError:

            print("NO VALUE FOR %s", attribute)
            return None

    def get_next_file(self, file_type: FileTypes = FileTypes.html,
                      return_path: bool = False) -> Tuple[str, AnyStr]:
        """Generic function for unpacking and getting content for further scrapping.
        There is an exception for getting path to the to-be-scrapped file, because some scrappers
        needs the date of the file when it was scrapped"""
        base_dir = Helper.get_access_to_environment()
        html_raws = Helper.join_dir_base(dir=base_dir, basename=self.config_path)
        file_to_process = f"{html_raws}/*.{file_type.name}"

        for path in glob.glob(file_to_process):
            _, filename = os.path.split(path)
            project_name = filename.split('.')[0]
            if return_path:
                yield project_name, path
            else:
                content = Helper.open_file(path=path)
                yield project_name, content


