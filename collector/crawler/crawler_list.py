# import standard
import datetime

import pandas as pd
# import third-party
from tqdm import tqdm
# import own
from .base_crawler import BaseCrawler
from utils import get_save_path, Helper


class IEOListCrawler(BaseCrawler):
    """data_scraper
    Gets the detail information about each company like website, description and location"""

    INITIAL_URL = 'https://icobench.com/ieo'

    def __init__(self):
        super().__init__(use_selenium=True)

    @get_save_path(path='data_raw/ieo_list_raw_html')
    def crawl_pages(self, save_point):
        self.get(self.INITIAL_URL)
        self.scroll_to_the_end_html()
        path_to_save = Helper.join_dir_base(dir=save_point, basename='raw_list.html')
        Helper.save_file(save_path=path_to_save, content=self.driver.page_source)
