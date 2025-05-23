import allure

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as ec


class DashboardPage(BasePage):
    PAGE_URL = Links.DASHBOARD_PAGE

    MY_INFO_BUTTON = ("xpath", "//span[text()='My Info']")

    @allure.step("Click on my Info Link")
    def click_my_info_link(self):
        self.wait.until(ec.element_to_be_clickable(self.MY_INFO_BUTTON)).click()
