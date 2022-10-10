from selenium import webdriver
import os

from bs4 import BeautifulSoup

import pandas as pd

from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True






class setUp:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(executable_path = r"C:/Users/user/Desktop/Desktop/Sides/chromedriver.exe")
        

    def getWeb(self, URL):
        self.driver.get(URL)

    def bsgetDOM(self, URL):
        # self.driver.get(URL)
        self.soup = BeautifulSoup(self.driver.page_source)
        # print(BeautifulSoup(self.driver.page_source))

    def getData(self):

        self.siblings = self.soup.find_all("a")
        text = 'Cited by'
        # print(siblings)

        x = []

        # f = []

        for i in self.siblings:
            if(text in str(i)):
                x.append(i.string)
        # print(x)

        return x

        #titleDF = pd.DataFrame(x, columns = ['Citations'])
        # print(titleDF)

        # print(titleDF)


        
        

    # def scrapeCitation(self, title):
    #     self.soup.find_next_siblings()

        # C:\Users\user\Envs\scrapers\Lib\site-packages\selenium\webdriver\chrome
        # Users/user/Envs/scrapers/Lib/site-packages/selenium/webdriver/chromium