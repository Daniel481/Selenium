from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def openLoginpage(self):
        self.driver.find_element(by=By.XPATH, value="//button[text()='Log In']").click()
        self.driver.implicitly_wait(10)
        self.driver.switch_to.frame("disneyid-iframe")
        return self

    def enterEmail(self, email):
        self.driver.find_element(by=By.XPATH, value="//input[@aria-label='Username or Email Address']").send_keys(email)
        return self

    def enterPassword(self, password):
        self.driver.find_element(by=By.XPATH, value="//input[@autocomplete='current-password']").send_keys(password)
        return self

    def clickLogin(self):
        self.driver.find_element_by_xpath("//button[text()='Log In']").click()
