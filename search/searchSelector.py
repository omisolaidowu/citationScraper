from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

class webSelectors:
    searchBox = "//input[@id='gs_hdr_tsi']"


select = webSelectors()
class webActions:
    def __init__(self, driver) -> None:
        self.driver = driver

    def searchItem(self, title):
        return self.driver.find_element(By.XPATH, select.searchBox).send_keys(title, Keys.ENTER)
        
