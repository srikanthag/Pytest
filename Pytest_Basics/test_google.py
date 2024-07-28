from selenium import webdriver
import pytest

driver = None


def google_setup():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://www.google.com")


def google_teardown():
    driver = webdriver.Chrome()
    driver.quit()


def google_testcase_01():
    driver = webdriver.Chrome()
    assert driver.title == "Google"


def google_testcase_02():
    driver = webdriver.Chrome()
    assert driver.current_url == "google.com"
