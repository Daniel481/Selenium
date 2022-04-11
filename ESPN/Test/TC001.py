import time
import unittest

import HtmlTestRunner
from selenium import webdriver

from ESPN.Pages.FollowPage import Followpage
from ESPN.Pages.Loginpage import LoginPage
from ESPN.Pages.SearchPage import SearchPage
from ESPN.Pages.SignupPage import SignUpPage


class TC001(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="./ESPN/Driver/chromedriver.exe")
        cls.driver.delete_all_cookies()
        cls.driver.maximize_window()
        cls.driver.get("https://www.espn.in/")
        cls.driver.implicitly_wait(5)

    def test_signup(self):
        driver = self.driver
        sign_up = SignUpPage(driver)
        sign_up.openSignUpPage()
        sign_up.enterFirstName("Test")
        sign_up.enterLastName("Name")
        sign_up.enterEmail("dbxd78x@btcmod.com")
        sign_up.enterPassword("Test@123")
        time.sleep(10)

    def test_login(self):
        driver = self.driver
        login = LoginPage(driver)
        login.openLoginpage()
        login.enterEmail("dbxd78x@btcmod.com")
        login.enterPassword("Test@123")
        time.sleep(10)

    def test_search(self):
        driver = self.driver
        search = SearchPage(driver)
        search.searchKeyword("FootBall")
        time.sleep(5)

    def test_Follow(self):
        driver = self.driver
        search = SearchPage(self.driver)
        search.searchKeyword("FootBall")
        follow = Followpage(driver)
        follow.FollowFootBallTeam()
        time.sleep(5)

    @classmethod
    def tearDown(cls):
        time.sleep(10)
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./ESPN/Reports"))
