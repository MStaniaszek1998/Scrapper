from tqdm import tqdm
from lxml import html
import pandas as pd
from .scrapper_base import ScrapperBase
from utils import Helper,get_save_path


class IeosProfilesScrapper(ScrapperBase):

    def __init__(self):
        self.get_raw_html = "data_raw/ieo_profiles_raw_html"
        super().__init__(path_to_scrapped=self.get_raw_html)

    def parse_file(self,content,name):
        root = html.fromstring(content)
        xpath_to_table = '//*[@id="whitepaper"]/p[1]/object/@data'
        whitepaper_url = self._check_if_attr_exists(xpath=xpath_to_table,root=root,
                                                   attribute='whitepaper_url')


        return [whitepaper_url,name]

    @get_save_path(path='data_scrapped/ieo_profiles_scrapped')
    def parse_files(self,save_point):
        frames = []
        columns = ['whitepaper_url', 'Project_name']
        for project_name,content in tqdm(self.get_next_file()):

            frames.append(self.parse_file(content=content,name=project_name))
        save_path = Helper.join_dir_base(save_point,'scrapped_ieos_profiles.csv')
        self.scrapped_list_path = save_path
        df = pd.DataFrame(data=frames,columns=columns)
        Helper.write_df_to_csv(path=save_path,content=df)