import time

from selenium.webdriver.common.keys import Keys
from POM.Locators.Locators import Locators

class Registration_Page:
    def __init__(self, driver):
        self.driver = driver
        self.select_gender_using_id = Locators.select_gender_using_id
        self.firstname_using_id = Locators.firstname_using_id
        self.lastname_using_id = Locators.lastname_using_id
        self.email_using_id = Locators.email_using_id
        self.password_using_id = Locators.password_using_id
        self.confirm_password_using_id = Locators.confirm_password_using_id
        self.registration_button_using_id = Locators.registration_button_using_id


    def Click_Gender(self):
        Select_Gender = self.driver.find_element("id", self.select_gender_using_id)
        Select_Gender.click()
        time.sleep(1)

    def Enter_Firstname(self, username):
        Enter_First_Name = self.driver.find_element("id", self.firstname_using_id)
        Enter_First_Name.clear()
        Enter_First_Name = self.driver.find_element("id", self.firstname_using_id)
        Enter_First_Name.send_keys(username, Keys.ENTER)
        time.sleep(1)

    def Enter_Lastname(self, username2):
        Enter_Last_Name = self.driver.find_element("id", self.lastname_using_id)
        Enter_Last_Name.clear()
        Enter_Last_Name = self.driver.find_element("id", self.lastname_using_id)
        Enter_Last_Name.send_keys(username2, Keys.ENTER)
        time.sleep(1)

    def Enter_Email(self, email):
        Enter_Email = self.driver.find_element("id", self.email_using_id)
        Enter_Email.send_keys(email, Keys.ENTER)
        time.sleep(1)

    def Enter_Password(self, password):
        Enter_Password = self.driver.find_element("id", self.password_using_id)
        Enter_Password.send_keys(password, Keys.ENTER)
        time.sleep(1)

    def Enter_Confirm_Password(self, password2):
        Enter_Password = self.driver.find_element("id", self.confirm_password_using_id)
        Enter_Password.send_keys(password2, Keys.ENTER)
        time.sleep(1)

    def Click_Reg_button(self):
        Click_Register = self.driver.find_element("id", self.registration_button_using_id)
        Click_Register.click()
        time.sleep(5)





