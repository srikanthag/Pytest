from selenium import webdriver

def test_google():
    driver = webdriver.Chrome(r'C:\Users\hp\Desktop\IT\Testing\Frameworks\Pytest\Chromedriver\chromedriver-win64\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://www.google.com")
    assert driver.title == "Google"
    driver.quit()


# def test_facebook():
#     driver = webdriver.Chrome(r"C:\Users\hp\Desktop\IT\Testing\Frameworks\Pytest\Chromedriver\chromedriver-win64\chromedriver.exe")
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     driver.get("http://www.facebook.com")
#     assert driver.title == "Facebook"
#     driver.quit()










