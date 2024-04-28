from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from POM.Pages.Login_page import Login_Page


class Login_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r"C:\Users\hp\Desktop\IT\Testing\Frameworks\Pytest\Chromedriver\chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()


    def test_login(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/login")
        time.sleep(5)
        login = Login_Page(driver)
        login.Enter_Email("srikanth1945@gmail.com")
        login.Enter_Password("123456")
        login.Click_Login()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")