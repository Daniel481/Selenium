import time
import unittest

import HtmlTestRunner
from selenium import webdriver

from ESPN.Pages.FollowPage import Followpage
from ESPN.Pages.Loginpage import LoginPage
from ESPN.Pages.SearchPage import SearchPage
from ESPN.Pages.SignupPage import SignUpPage
from ESPN.Pages.ReadExcel import ReadExcel

tc = unittest.TestCase()
ReadExcel.read_excel()


class TC001(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="./ESPN/Driver/chromedriver.exe")
        cls.driver.delete_all_cookies()
        cls.driver.maximize_window()
        cls.driver.get("https://www.espn.in/")
        cls.driver.implicitly_wait(10)
        actual_title = "ESPN: Serving sports fans. Anytime. Anywhere."
        expected_title = cls.driver.title
        tc.assertEqual(actual_title, expected_title, msg="Title Mismatch")
        time.sleep(5)

    def test_signup(self):
        try:
            driver = self.driver
            sign_up = SignUpPage(driver)
            driver.implicitly_wait(10)
            sign_up.openSignUpPage()
            sign_up.enterFirstName("Test")
            sign_up.enterLastName("Name")
            sign_up.enterEmail(ReadExcel.email[0])
            sign_up.enterPassword(ReadExcel.password[0])
            time.sleep(5)
        except:
            driver.refresh()
            time.sleep(5)
            self.test_signup()

    def test_login(self):
        try:
            driver = self.driver
            login = LoginPage(driver)
            login.openLoginpage()
            driver.implicitly_wait(10)
            login.enterEmail(ReadExcel.email[0])
            login.enterPassword(ReadExcel.password[0])
            time.sleep(5)
        except:
            driver.refresh()
            time.sleep(5)
            self.test_login()

    def test_search(self):
        try:
            driver = self.driver
            search = SearchPage(driver)
            self.driver.implicitly_wait(10)
            search.searchKeyword("FootBall")
            time.sleep(5)
        except:
            driver.refresh()
            time.sleep(5)
            self.test_search()

    def test_Follow(self):
        try:
            driver = self.driver
            search = SearchPage(self.driver)
            self.driver.implicitly_wait(10)
            search.searchKeyword("FootBall")
            follow = Followpage(driver)
            follow.FollowFootBallTeam()
            time.sleep(5)
        except:
            driver.refresh()
            time.sleep(5)
            self.test_Follow()

    @classmethod
    def tearDown(cls):
        time.sleep(10)
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./ESPN/Reports"))
