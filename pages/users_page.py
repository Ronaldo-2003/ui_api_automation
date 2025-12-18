from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class UsersPage(BasePage):
    TABLE_ROWS = (By.TAG_NAME, "tr")

    def get_rows(self):
        return self.driver.find_elements(*self.TABLE_ROWS)
