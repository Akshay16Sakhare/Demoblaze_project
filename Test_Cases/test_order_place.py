import time
from selenium.webdriver.common.alert import Alert
from Test_Cases.conftest import setup
from POM_Demo_blaze.DemoBlaze_POM import Demo_Blaze_ele
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilities.readConfig import Read_values

class Test_order_place():

    userName = Read_values.get_username()
    passWord = Read_values.get_password()

    name = Read_values.get_Name_for_order()
    country = Read_values.get_country()
    city = Read_values.get_city()
    credit_card_No = Read_values.get_creditCard_No()
    month = Read_values.get_month()
    year = Read_values.get_year()

    @property
    def wait(self):
        return WebDriverWait(self.driver, 5)

    def test_order_placing(self, setup):
        self.driver = setup
        self.login = Demo_Blaze_ele(self.driver)
        self.driver.implicitly_wait(5)
        self.login.click_login_opt()
        self.login.enter_login_userName(self.userName)
        self.login.enter_login_passWord(self.passWord)
        self.login.click_login_button()
        time.sleep(3)
        my_products = [self.login.product_1_selector, self.login.product_2_selector]

        for item in my_products:
            self.wait.until(EC.presence_of_element_located(item)).click()
            self.login.add_products()
            time.sleep(2)
            self.driver.switch_to.alert.accept()
            time.sleep(2)
            self.login.click_home_button()

        self.login.go_to_cart()
        print("Products added to cart.")

        time.sleep(2)
        total = self.wait.until(EC.presence_of_element_located((By.XPATH, "//h3[@id='totalp']"))).text
        print("Your Total Amount To Pay : "+'$'+total)

        self.login.click_place_order()
        time.sleep(3)
        self.login.Place_order_Name(self.name)
        self.login.Place_order_Country(self.country)
        self.login.Place_order_City(self.city)
        self.login.Place_order_Creditcard(self.credit_card_No)
        self.login.Place_order_Month(self.month)
        self.login.Place_order_Year(self.year)

        element1 = self.driver.find_element(By.XPATH, "//button[contains(text(),'Purchase')]")
        self.driver.execute_script("arguments[0].click();", element1)

        time.sleep(2)

        expected_message = 'Thank you for your purchase!'
        actual_message = self.driver.find_element(By.XPATH, "//h2[contains(text(),'Thank you for your purchase!')]").text
        if expected_message in actual_message and expected_message == actual_message:
            print("Order placed successfully.")
            assert True

        else:
            print("Sorry!! Try again.")
            assert False

        time.sleep(5)
        self.driver.close()







