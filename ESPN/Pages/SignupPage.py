import time

from selenium.webdriver.common.by import By


class SignUpPage():

    def __init__(self, driver):
        self.driver = driver

    def openSignUpPage(self):
        self.driver.find_element(by=By.XPATH, value="//button[text()='Sign Up']").click()
        self.driver.implicitly_wait(10)
        self.driver.switch_to.frame("disneyid-iframe")

    def enterFirstName(self, firstname):
        self.driver.find_element(by=By.XPATH, value="//input[@name='firstName']").send_keys(firstname)

    def enterLastName(self, lastName):
        self.driver.find_element(by=By.XPATH, value="//input[@name='lastName']").send_keys(lastName)

    def enterEmail(self, email):
        self.driver.find_element(by=By.XPATH, value="//input[@name='email']").send_keys(email)
        return self

    def enterPassword(self, password):
        self.driver.find_element(by=By.XPATH, value="//input[@name='newPassword']").send_keys(password)
        return self

    def clickSignUp(self):
        self.driver.find_element(by=By.XPATH, value="//button[text()='Sign Up']").click()
        return self

    def Search(self):
        self.driver.get("https://www.espn.in/")
        time.sleep(1)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="//a[@id='global-search-trigger']").click()
        self.driver.find_element(by=By.XPATH, value="//input[@id='global-search-input']").send_keys("FootBall")
        self.driver.find_element(by=By.XPATH, value="//input[@class='btn-search']").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="//a[@data-track-searchresultselected='Navy Football Club']").click()
        self.driver.find_element(by=By.XPATH, value="//button[text()='Follow']").click()

    def tearDown(self):
        time.sleep(10)
        self.driver.quit()
