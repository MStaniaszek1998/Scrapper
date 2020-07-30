# Scrapper - Crawler Architecture
The goal is to crawl the https://icobench.com/ieo page and collect information about Initial
Exchange Offerings. It collects the information about the IEOs and their whitepapers. 

## Architecture flow
1. Crawler sends a GET request to the website (by using either selenium or requests) and saves
 the web page html into Data Lake. 
2. Scrapper opens the downloaded files and scrapes the information (i.e. name of the IEOs, Rating
, url to the whitepaper) and saves the result into the data lake.
3. Inserter puts urls to database to maintain information about url's status of crawling. 
[Present with image]


## Data Lake Structure
Data Lake consists of raw crawled web pages or pdf files and also scrapped information into csv
 format.
There are two Data lakes; one for development purposes and the second for production.
Data Lake is divided into two separate folders: 
- **data_raw** - where all raw data is stored 
- **data_scrapped** - where the data is stored into csv format ready for further ETL processing. 

Data Raw has the following raw data:
- ieo_list_raw_html - contains only one html file with the list of all IEOs
- ieo_profiles_raw_html - contains a lot of html files with contents about each IEOs
- ieo_whitepapers - contains all downloaded pdf files from IEOs' profiles

Data Scrapped contains:
- **scrapped_ieos_list.csv** - file with information about each IEOs such as:<br>
[Input image schema]
- **scrapped_ieos_profiles.csv** - it contains scrapped information from profiles. Currently only
 url to whitepapers in order to download them. <br>
[Input image schema]

## 


 