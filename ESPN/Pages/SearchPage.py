from selenium.webdriver.common.by import By


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    def searchKeyword(self, keyword):
        self.driver.find_element(by=By.XPATH, value="//a[@id='global-search-trigger']").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(by=By.XPATH, value="//input[@id='global-search-input']").send_keys(keyword)
        self.driver.implicitly_wait(5)
        self.driver.find_element(by=By.XPATH, value="//input[@class='btn-search']").click()
