from pageObjects.login import login_Page
from utilities.readProperties import ReadConfig


class Test_001_login:
    baseUrl = ReadConfig.getApplicationURL()
    userName = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.login_obj = login_Page(self.driver)
        self.login_obj.click_login_button()
        self.driver.implicitly_wait(2)
        self.window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(self.window_after)
        self.login_obj.click_and_fill_mobile_number()
        self.login_obj.click_and_fill_password()
        self.login_obj.click_login_button_UI()
        self.login_obj.click_bunglao_name()
        self.login_obj.click_estimation_project_name()
        self.login_obj.Print_table_project()
        self.login_obj.total_amount()