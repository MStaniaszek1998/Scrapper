from crawler import IEOListCrawler,IeosProfilesCrawler,PDFWhitepaperCrawler
from scrapper import ScrapperIeosList,IeosProfilesScrapper









def main():
    print('Initialize folders:')


    print('COLLECT INITIAL LIST OF IEOs RAW HTML')
    ieo_crawler = IEOListCrawler()
    ieo_crawler.crawl_pages()
    print('SCRAPE THE LIST FROM RAW IEOS LIST')
    scrapper = ScrapperIeosList()
    scrapper.parse_files()
    print('CRAWL IEOS PROFILES - RAW HTML')
    ieo_profile_crawl = IeosProfilesCrawler()
    ieo_profile_crawl.crawl_pages()
    print('SCRAPE PROFILES INFORMATION ')
    scraper = IeosProfilesScrapper()
    scraper.parse_files()
    print('CRAWL PDF WHITEPAPERS')
    crawler = PDFWhitepaperCrawler()
    crawler.crawl_pages()




if __name__ == "__main__":
    main()