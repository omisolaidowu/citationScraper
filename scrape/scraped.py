import sys
sys.path.append(sys.path[0] + "/..")

from selSetup.setUp import setUp

from search.searchSelector import webActions
import pandas as pd
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class runner:

    def scrapeRunner(self):
        self.df = pd.read_excel(r"df_full.xlsx")
        self.titles = self.df["title"]

        # self.titles = self.myTitle[12:25]



        setup = setUp()

        action = webActions(setup.driver)




        citations = []

        for title in self.titles:
            setup.getWeb("https://scholar.google.com/")
            action.searchItem(title)
            time.sleep(10)
            setup.bsgetDOM(setup.driver.current_url)   
            # time.sleep(4)
            cites = setup.getData()

            print(cites)

            citations.append(cites)


        
        
        
        myCitations = sum(citations, [])
        print(myCitations)

        # print(myCitations)
        self.newDf = pd.DataFrame(myCitations, columns = ['Citations'])

        # print(self.newDf)

        self.newDf.to_excel('citationsMain.xlsx')
        

    # print(runner.citations)



# class webActions:
#     def gotoWeb()