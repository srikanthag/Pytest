import time

from selenium.webdriver.common.keys import Keys
from POM.Locators.Locators import Locators

class Login_Page:
    def __init__(self, driver):
        self.driver = driver
        self.enter_email_id = Locators.enter_email_id
        self.enter_password_id = Locators.enter_password_id
        self.click_login_button_xpath = Locators.click_login_button_xpath


    def Enter_Email(self, emailid):
        Enter_Email_Id = self.driver.find_element("id", self.enter_email_id)
        Enter_Email_Id.clear()
        Enter_Email_Id = self.driver.find_element("id", self.enter_email_id)
        Enter_Email_Id.send_keys(emailid, Keys.ENTER)
        time.sleep(1)

    def Enter_Password(self, password):
        Enter_Password = self.driver.find_element("id", self.enter_password_id)
        Enter_Password.click()
        Enter_Password = self.driver.find_element("id", self.enter_password_id)
        Enter_Password.clear()
        Enter_Password = self.driver.find_element("id", self.enter_password_id)
        Enter_Password.send_keys(password, Keys.ENTER)
        time.sleep(2)

    def Click_Login(self):
        click_login_button = self.driver.find_element("xpath", self.click_login_button_xpath)
        click_login_button.click()
        time.sleep(3)