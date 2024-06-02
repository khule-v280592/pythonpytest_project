from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.readProperties import ReadConfig


class login_Page:
    login_button = "//div[@class='linknbutton']//a[text()='LOGIN']"
    mobile_number_xpath = "//input[@id='mobileNumber']"
    continue_button = "//button[contains(text(),'Continue')]"
    password_xpath = "//input[@id='password']"
    login_button_xpath = "//button[text()=' Login ']"
    bungalow_name_xpath = "//span[text()=' Sample Bungalow Project G+1']"
    Estimation_name_xpath = "//p[text()=' Estimation by thumb rule-Economical specifications']"
    print_list_table_xpath = "//table[@aria-describedby='Quote Items']"
    total_amount_xpath = "//h2[@id='total-amount']"
    userName = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    def __init__(self, driver):
        self.driver = driver

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    def click_and_fill_mobile_number(self):
        self.driver.find_element(By.XPATH, self.mobile_number_xpath).click()
        self.driver.find_element(By.XPATH, self.mobile_number_xpath).send_keys(self.userName)
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Continue')]")))
        element.click()

    def click_and_fill_password(self):
        self.driver.find_element(By.XPATH, self.password_xpath).click()
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(self.password)

    def click_login_button_UI(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def click_bunglao_name(self):
        self.driver.find_element(By.XPATH, self.bungalow_name_xpath).click()

    def click_estimation_project_name(self):
        self.driver.find_element(By.XPATH, self.Estimation_name_xpath).click()

    def Print_table_project(self):
        p = self.driver.find_elements(By.XPATH, self.print_list_table_xpath)
        for i in p:
            print(i.text)

    def total_amount(self):
        total_amount = self.driver.find_element(By.XPATH, self.total_amount_xpath).text
        print(total_amount)
