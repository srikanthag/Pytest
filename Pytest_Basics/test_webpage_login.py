from selenium import webdriver


def test_google():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://www.google.com")
    assert driver.title == "Google"
    driver.quit()


def test_facebook():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://www.facebook.com")
    assert driver.title == "Facebook – log in or sign up"
    driver.quit()



def test_amezon():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://www.amezon.com")
    assert driver.title == "amezon"
    driver.quit()






