from selenium.webdriver.common.by import By


class Followpage:

    def __init__(self, driver):
        self.driver = driver

    def FollowFootBallTeam(self):
        self.driver.implicitly_wait(3)
        self.driver.find_element(by=By.XPATH,
                                 value="//a[@data-track-searchresultselected='Navy Football Club']").click()
        self.driver.find_element(by=By.XPATH, value="//button[text()='Follow']").click()
