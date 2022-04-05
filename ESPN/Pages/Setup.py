from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver

class Setup:
    driver = None


    def LaunchBrowser(self, str):
        if(str.lower()=="chrome"):
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif(str.lower()=="firefox"):
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.delete_all_cookies()
        driver.maximize_window()
        driver.get("https://www.espn.in/")
        driver.implicitly_wait(5)
        return driver
    
    def CloseDriver():
        global driver
        driver.quit()