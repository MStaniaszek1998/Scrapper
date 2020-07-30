from crawler import IEOListCrawler,IeosProfilesCrawler,PDFWhitepaperCrawler
from scrapper import ScrapperIeosList,IeosProfilesScrapper
from utils import Inserter









def main():
    print('Initialize folders:')


    print('COLLECT INITIAL LIST OF IEOs RAW HTML')
    ieo_crawler = IEOListCrawler()
    ieo_crawler.crawl_pages()
    print('SCRAPE THE LIST FROM RAW IEOS LIST')
    scrapper = ScrapperIeosList()
    scrapper.parse_files()
    insert_profiles = Inserter(csv_to_insert=scrapper.scrapped_list_path,col_url='links')
    insert_profiles.insert_url_to_database(crawler_name='IEOListCrawler')
    print('CRAWL IEOS PROFILES - RAW HTML')
    ieo_profile_crawl = IeosProfilesCrawler()
    ieo_profile_crawl.crawl_pages()
    print('SCRAPE PROFILES INFORMATION ')
    scrapper = IeosProfilesScrapper()
    scrapper.parse_files()
    insert_profiles = Inserter(csv_to_insert=scrapper.scrapped_list_path,col_url='whitepaper_url')
    insert_profiles.insert_url_to_database(crawler_name='IeosProfilesCrawler')
    print('CRAWL PDF WHITEPAPERS')
    crawler = PDFWhitepaperCrawler()
    crawler.crawl_pages()




if __name__ == "__main__":
    main()