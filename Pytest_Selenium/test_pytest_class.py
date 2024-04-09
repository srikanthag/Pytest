from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pytest

class Test_sample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(r"C:\Users\hp\Desktop\IT\Testing\Selenium_Class\Chromedriver\chromedriver.exe")
        time.sleep(3)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test completed")

    def test_search(self,test_setup):
        driver.get("https://www.google.co.in")
        time.sleep(10)
        search_input = driver.find_element("name", "q")
        search_input.send_keys('Rohit Sharma', Keys.ENTER)
        time.sleep(5)
        s = driver.title
        assert s == "Rohit Sharma - Google Search"

    # print("Title:", driver.title)
    # print("URL:", driver.current_url)

    # def test_teardown():
    #     driver.close()      # close current browser
    #     driver.quit()       # close all browser