import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from sys import argv
from time import sleep
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm

BASE_URL = 'https://ghosttown.deadface.io/'
PATH_TO_WEBDRIVER = os.path.join('chromedriver_win32', 'chromedriver.exe')

class Scraper:
    def __init__(self, base_url, headless: bool = False):
        self.base_url = base_url
        self.article_list = dict()
        self.article_url_list = []
        self.init_browser(headless=headless)
        if self.browser.title == 0:
            raise Exception(f'Browser could not reach {self.base_url}')
    
    def init_browser(self, headless: bool = False):
        if headless:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            self.browser = webdriver.Chrome(executable_path=PATH_TO_WEBDRIVER, options=chrome_options)
        else:
            self.browser = webdriver.Chrome(executable_path=PATH_TO_WEBDRIVER)
        self.browser.get(self.base_url)

    def get_all_articles_content(self):
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
        for url in tqdm(self.article_url_list, desc="Extracting raw content of articles..."):
            self.browser.get(url)
            sleep(10)
            self.article_list[url] = self.browser.page_source

    def search_keywords(self, keywords: list):
        for url in self.article_list:
            for keyword in keywords:
                if keyword.lower() in self.article_list[url].lower():
                    print(f'Keyword : {keyword}, URL : {url}')

if __name__ == '__main__':
    args = argv[1:]
    #with open('..\\SQL\\extracted_users.txt', 'r') as f:
    #    lines = f.readlines()
    #    lines = [l.strip() for l in lines]
    # For SQL challenge
    if len(args) < 1:
        print('You should provide at least one keyword to ')
    scraper = Scraper(BASE_URL, headless=True)
    sleep(15)
    scraper.get_all_articles_content()
    scraper.extract_raw_articles()
    scraper.search_keywords(args)