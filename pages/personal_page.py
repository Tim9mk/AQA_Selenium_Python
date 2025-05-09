import allure

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys


class PersonalPage(BasePage):
    PAGE_URL = Links.PERSONAL_PAGE

    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    SAVE_BUTTON = ("xpath", "//button[@type='submit'][1]")
    SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")

    def __init__(self, driver):
        super().__init__(driver)
        self.name = ""

    def change_name(self, new_name):
        with allure.step(f"change name on {new_name}"):
            first_name_field = self.wait.until(ec.element_to_be_clickable(self.FIRST_NAME_FIELD))
            first_name_field.send_keys(Keys.COMMAND + "A")
            first_name_field.send_keys(Keys.BACKSPACE)
            first_name_field.send_keys(new_name)
            self.name = new_name

    @allure.step("Save changes")
    def save_changes(self):
        self.wait.until(ec.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Changes has been saved successfully")
    def is_changes_saved(self):
        self.wait.until(ec.invisibility_of_element_located(self.SPINNER))
        self.wait.until(ec.visibility_of_element_located(self.FIRST_NAME_FIELD))
        self.wait.until(ec.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name))



