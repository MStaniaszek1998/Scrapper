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

    @get_save_path(path='data_raw/ieo_whitepapers_metadata')
    @get_ieos_list(path="data_scrapped/ieo_profiles_scrapped/scrapped_ieos_profiles.csv")
    def crawl_pages(self, save_point, ieos_list):
        cols = ['Project_name', 'whitepaper_url', 'DOWNLOAD_STATUS']
        statuses = []
        print(ieos_list)
        for _, row in tqdm(ieos_list.iterrows()):
            print(f'CRAWLING FOR {row["Project_name"]} ')
            status = self.download_page(row=row, save_base=save_point)
            statuses.append(status)
        ieos_list['DOWNLOAD_STATUS'] = statuses
        path_to_save = Helper.join_dir_base(save_point, 'metadata_scrapped_whitepapers.csv')
        Helper.write_df_to_csv(content=ieos_list[cols], path=path_to_save)

    def download_page(self, row, save_base):

        try:

            response = self.get(row['whitepaper_url'], stream=True)

            path_to_save = Helper.join_dir_base(save_base, f"{row['Project_name']}.pdf")
            Helper.save_file(save_path=path_to_save, content=response, stream_file=True)
            return 'SUCCESS'
        except:
            return 'FAILED'


