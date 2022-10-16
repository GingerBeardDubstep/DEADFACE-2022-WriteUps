import os
import json
from selenium import webdriver
from sys import argv
from time import sleep
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

BASE_URL = 'https://ghosttown.deadface.io/'
PATH_TO_WEBDRIVER = os.path.join('chromedriver_win32', 'chromedriver.exe')
POTFILE = 'contents.json'

class Scraper:
    def __init__(self, base_url, headless: bool = False):
        self.base_url = base_url
        self.article_list = dict()
        self.article_url_list = []
        self.init_browser(headless=headless)
        if self.browser.title == 0:
            raise Exception(f'Browser could not reach {self.base_url}')
    
    def init_browser(self, headless: bool = False, disable_log: bool = True):
        chrome_options = Options()
        if disable_log:
            chrome_options.add_argument("--log-level=3")
        if headless:
            chrome_options.add_argument("--headless")
        self.browser = webdriver.Chrome(executable_path=PATH_TO_WEBDRIVER, options=chrome_options)
        self.browser.get(self.base_url)

    def get_all_articles_content(self) -> list:
        article_list = self.browser.execute_script('''var my_ul = document.getElementsByTagName('ul')[2];
var article_list = my_ul.getElementsByTagName('li');
var res = [];
for(var i=0; i < article_list.length; i++){
    res.push(article_list[i].children[0].children[0].children[0].href);
}
return(res);''')
        article_list = [a for a in article_list if a is not None and a != 'None']
        self.article_url_list = article_list
        return article_list

    def extract_raw_articles(self):
        for url in tqdm(self.article_url_list, desc="Crawling articles..."):
            self.browser.get(url)
            sleep(10)
            self.article_list[url] = self.browser.page_source

    def search_keywords(self, keywords: list):
        report = ''
        for url in self.article_list:
            for keyword in keywords:
                if keyword.lower() in self.article_list[url].lower():
                    report += f'Keyword : {keyword}, URL : {url}\n'
        if len(report) == 0:
            print(f"No article was found about the keywords '{keywords}'")
        else:
            print(f'Some keywords have been found in articles :\n{report[:-1]}')
    
    def check_content_already_extracted(self) -> bool:
        if os.path.exists(POTFILE):
            return True
        return False

    def load_potfile(self):
        with open(POTFILE, 'r') as f:
            self.article_list = json.loads(f.read())

    def write_potfile(self):
        with open(POTFILE, 'w') as f:
            f.write(json.dumps(self.article_list))

if __name__ == '__main__':
    args = argv[1:]
    #with open('..\\SQL\\extracted_users.txt', 'r') as f:
    #    lines = f.readlines()
    #    lines = [l.strip() for l in lines]
    # For SQL challenge : replace "args" line 86 by "lines" and uncomment the three previous lines
    if len(args) < 1:
        print('You should provide at least one keyword to ')
    scraper = Scraper(BASE_URL, headless=True)
    if not scraper.check_content_already_extracted():
        print('No potfile found\nLaunching scraper')
        sleep(15)
        scraper.get_all_articles_content()
        scraper.extract_raw_articles()
        scraper.write_potfile()
    else:
        print('Loading potfile')
        scraper.load_potfile()
    scraper.search_keywords(args)