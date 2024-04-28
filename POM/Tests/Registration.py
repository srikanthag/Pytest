from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from POM.Pages.Registration_page import Registration_Page


class Registration_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r"C:\Users\hp\Desktop\IT\Testing\Frameworks\Pytest\Chromedriver\chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_registartion(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/register")
        time.sleep(5)
        registration = Registration_Page(driver)
        registration.Click_Gender()
        registration.Enter_Firstname("Rohit1")
        registration.Enter_Lastname("Sharma1")
        registration.Enter_Email("Rsharma@gmail.com")
        registration.Enter_Password("123456789")
        registration.Enter_Confirm_Password("123456789")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")





