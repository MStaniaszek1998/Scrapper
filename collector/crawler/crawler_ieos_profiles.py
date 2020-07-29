from tqdm import tqdm
from .base_crawler import BaseCrawler
from utils import get_save_path,get_ieos_list,Helper


class IeosProfilesCrawler(BaseCrawler):

    def __init__(self):
        super().__init__(use_selenium=True)

    @get_save_path(path='data_raw/ieo_profiles_raw_html')
    @get_ieos_list(path="data_scrapped/ieo_list_scrapped/scrapped_ieos_list.csv")
    def crawl_pages(self, save_point, ieos_list):

        for _, row in tqdm(ieos_list.iterrows()):
            print(f'COLLECTING RAW FOR {row["Project_Name"]}')
            url_to_scrape = Helper.create_url(extended_path=row['links'])
            self.get(url_to_scrape)
            self.scroll_to_the_end_html()
            path_to_save = Helper.join_dir_base(save_point, f"{row['Project_Name']}.html")
            Helper.save_file(save_path=path_to_save, content=self.driver.page_source)
