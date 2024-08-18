from page_objects.base_page import BasePage
from locators.locators import MainPageLocators, PersonalAccountLocators


class PersonalAccountPage(BasePage):

    def click_pers_acc_button_on_main(self):
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT)

    def click_order_list(self):
        self.click_element(PersonalAccountLocators.ORDERS_LIST_LINK)

    def click_exit_link(self):
        self.click_element(PersonalAccountLocators.EXIT_LINK)

    def click_profile_settings(self):
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT)