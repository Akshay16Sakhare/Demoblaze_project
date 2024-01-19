import time
from selenium.webdriver.common.alert import Alert
from Test_Cases.conftest import setup
from POM_Demo_blaze.DemoBlaze_POM import Demo_Blaze_ele

class Test_Login():

    def test_login(self, setup):
        self.driver = setup
        self.login = Demo_Blaze_ele(self.driver)
        self.driver.implicitly_wait(5)
        self.login.click_login_opt()
        self.login.enter_login_userName("akshay16")
        self.login.enter_login_passWord("testing@123")
        self.login.click_login_button()

        time.sleep(10)

        self.driver.close()

