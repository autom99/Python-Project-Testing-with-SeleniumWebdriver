import time

from selenium import webdriver

from SampleProjects.POMProhectDemo.Pages.homePage import HomePage
from SampleProjects.POMProhectDemo.Pages.loginPage import LoginPage

# try:
#     from StringIO import StringIO
# except ImportError:
#     from io import StringIO

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options,
                          executable_path='D:/Testing Purpose/Pycharm Testing/Selenium/Driver/chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()

try:
    driver.get('https://opensource-demo.orangehrmlive.com/')

    # Call method / Actions from Class
    login = LoginPage(driver)
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()

    homepage = HomePage(driver)
    homepage.click_welcome()
    homepage.click_logout()

    # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
    # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
    # self.driver.find_element_by_id("btnLogin").click()
    # self.driver.find_element_by_id("welcome").click()
    # self.driver.find_element_by_link_text("Logout").click()
    time.sleep(2)
    print("Test Completed successfully..!!")

finally:
    driver.close()
    driver.quit()
