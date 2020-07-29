"""Base Class for all scrapers.
Ensures the connection between data_collector and selenium one docker image using ip address.
It includes helper methods for each scraper i.e. maintains the session between scraper and
selenium, and gives access to generic functions for each scrapper"""
# import standard
import os
# import third-party
import random
import sys
import time
from datetime import datetime
from typing import Union, AnyStr

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys



class BaseScraper:
    """BaseScraper
    All scrapers derived from this class.
    It gives the scrappers the acces to the: selenium's webdriver and maintins its session;
    tokenization system responsible for fault-tolerant scrapping; common JavaScript actions for
    each scrapper."""

    def __init__(self, use_selenium: bool = True,
                 source_name: str = __name__, threshold_value: int = None):
        print("Starting Scrapping")
        self.source_name: str = source_name
        self._use_selenium = use_selenium
        self.threshold_value: int = threshold_value
        if use_selenium:
            self.driver = webdriver.Remote('http://172.17.0.1:4444/wd/hub',
                                           DesiredCapabilities.CHROME)




    def save_file(self, save_path: str, content: AnyStr, do_threshold: bool = False,
                  row: pd.Series = None) -> None:
        """Special function with threshold value to save the content if the size is above the
        threshold. Otherwise do not save the content and mark scrapped file as failed status at
        tokenization system"""

        DataSource.save_file(save_path=save_path, content=content)





    def scroll_to_the_end_html(self) -> None:
        """Webdriver is scrolling to the end of the webpage and renders the content for the
        further scrapping."""
        html = self.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)

    def renew_session(self) -> None:
        """If the error occurs the session with the docker selenium is renewed in order to avoid
        further errors from the website"""
        self.driver.quit()
        self.driver = webdriver.Remote('http://172.17.0.1:4444/wd/hub', DesiredCapabilities.CHROME)

    def __del__(self):
        """When the destructor is called it ends the session if its open"""
        if self._use_selenium:
            print("Ending Scrapping")
            self.driver.quit()

    @staticmethod
    def _sleep_randomize_duration(duration: int = 1, variance: float = 0.5) -> None:
        """Calculates the exact time how long to sleep.
        So having the duration equal to 1 and variance 0.5, it chooses the random number from 50
        to 150, and later divides by 100 to maintain the reasonable time.
        """
        low = (duration - variance) * 100
        high = (duration + variance) * 100
        return time.sleep(random.randint(low, high) / 100)

    @classmethod
    def sleep(cls, duration: int = 1, variance: Union[bool, float] = False) -> None:
        """Specifies how long the scrapping session has to wait for the further scrapping in
        order to avoid getting banned"""
        if not variance:
            time.sleep(duration)
        else:
            cls._sleep_randomize_duration(duration, variance)

