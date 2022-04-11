
import HtmlTestRunner
from selenium import webdriver
import ESPN.TestData.ReadExcel
from ESPN.Pages.FollowPage import Followpage
from ESPN.Pages.Loginpage import LoginPage
from ESPN.Pages.SearchPage import SearchPage
from ESPN.Pages.SignupPage import SignUpPage


read_excel()


class TC001(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(
            executable_path="C:/Users/Danny/PycharmProjects/Selenium/ESPN/Driver/chromedriver.exe")
        cls.driver.delete_all_cookies()
        cls.driver.maximize_window()
        cls.driver.get("https://www.espn.in/")
        cls.driver.implicitly_wait(10)
        actual_title = "ESPN: Serving sports fans. Anytime. Anywhere."
        expected_title = cls.driver.title
        tc.assertEqual(actual_title, expected_title, msg="Title Mismatch")
        cls.driver.implicitly_wait(10)

    def test_signup(self):
        try:
            driver = self.driver
            sign_up = SignUpPage(driver)
            sign_up.openSignUpPage()
            sign_up.enterFirstName("Test")
            sign_up.enterLastName("Name")
            sign_up.enterEmail(email[0])
            sign_up.enterPassword(password[0])
            driver.implicitly_wait(10)
        except:
            driver.refresh()
            driver.implicitly_wait(20)
            self.test_signup()

    def test_login(self):
        try:
            driver = self.driver
            login = LoginPage(driver)
            login.openLoginpage()
            login.enterEmail(email[0])
            login.enterPassword(password[0])
            driver.implicitly_wait(10)
        except:
            driver.refresh()
            driver.implicitly_wait(20)
            self.test_login()

    def test_search(self):
        try:
            driver = self.driver
            search = SearchPage(driver)
            search.searchKeyword("FootBall")
            self.driver.implicitly_wait(10)
        except:
            driver.refresh()
            driver.implicitly_wait(20)
            self.test_search()

    def test_Follow(self):
        try:
            driver = self.driver
            search = SearchPage(self.driver)
            search.searchKeyword("FootBall")
            follow = Followpage(driver)
            follow.FollowFootBallTeam()
            self.driver.implicitly_wait(10)
        except:
            driver.refresh()
            driver.implicitly_wait(20)
            self.test_Follow()

    @classmethod
    def tearDown(cls):
        cls.driver.implicitly_wait(10)
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./ESPN/Reports"))
