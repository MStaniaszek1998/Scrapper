# import standard
import datetime

import pandas as pd
# import third-party
from tqdm import tqdm
# import own
from .base_crawler import BaseCrawler
from utils import get_save_path, Helper, get_ieos_list


class PDFWhitepaperCrawler(BaseCrawler):

    def __init__(self):
        super().__init__(use_selenium=False)

    @get_save_path(path='data_raw/ieo_whitepapers_pdf')
    @get_ieos_list(crawler='IeosProfilesCrawler')
    def crawl_pages(self, save_point, ieos_list):
        print(ieos_list)
        for _, row in tqdm(ieos_list.iterrows()):
            print(f'CRAWLING FOR {row["project"]} ')
            self.download_page(row=row, save_base=save_point)

    def download_page(self, row, save_base):

        try:

            response = self.get(row['url'], stream=True)

            path_to_save = Helper.join_dir_base(save_base, f"{row['project']}.pdf")
            Helper.save_file(save_path=path_to_save, content=response, stream_file=True)
            self.report_success_url(url=row['url'])

        except:
            self.report_failure_url(url=row['url'])
