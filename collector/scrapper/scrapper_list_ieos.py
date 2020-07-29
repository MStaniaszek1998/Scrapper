
from lxml import html
import pandas as pd
from .scrapper_base import ScrapperBase
from utils import Helper,get_save_path


class ScrapperIeosList(ScrapperBase):
    def __init__(self):
        self.get_raw_html = 'data_raw/ieo_list_raw_html'
        super().__init__(path_to_scrapped=self.get_raw_html)

    def get_links(self,root):
        links_xpath = "//a[@class='name notranslate']/@href"
        links = self._check_if_attr_exists(xpath=links_xpath,root=root,attribute='links',
                                           return_all_join=True)
        links_list = links.split('~')

        return links_list

    def parse_file(self,content):
        root = html.fromstring(content)
        xpath_to_table = '//*[@id="ieocols"]/div/div/table'
        table_element = self._check_if_attr_exists(xpath=xpath_to_table,root=root,
                                                   attribute='all_table')
        table_conent = html.tostring(table_element)
        dataframe = pd.read_html(table_conent)[0]

        dataframe['links'] = self.get_links(root=root)
        dataframe = dataframe.drop(['Review', 'Project'], axis=1)
        dataframe = dataframe.rename(columns={"Project.1": "Project_Name"})
        return dataframe

    @get_save_path(path='data_scrapped/ieo_list_scrapped')
    def parse_files(self,save_point):
        frames = []

        for _,content in self.get_next_file():
            frames.append(self.parse_file(content=content))
        save_path = Helper.join_dir_base(save_point,'scrapped_ieos_list.csv')
        Helper.write_df_to_csv(path=save_path,content=frames[0])
