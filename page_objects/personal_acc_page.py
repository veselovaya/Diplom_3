from page_objects.base_page import BasePage
from locators.locators import MainPageLocators, PersonalAccountLocators
import allure


class PersonalAccountPage(BasePage):

    @allure.step('Переход на страницу ЛК')
    def click_pers_acc_button_on_main(self):
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT)

    @allure.step('Переход в Историю заказов')
    def click_order_list(self):
        self.click_element(PersonalAccountLocators.ORDERS_LIST_LINK)

    @allure.step('Выход из аккаунта в ЛК')
    def click_exit_link(self):
        self.click_element(PersonalAccountLocators.EXIT_LINK)

    @allure.step('Переход в Профиль ЛК')
    def click_profile_settings(self):
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT)

    @allure.step('Получить номер заказа в Истории заказов')
    def check_order_number_in_account(self):
        return self.get_actually_text(PersonalAccountLocators.ORDER_NUMBER_IN_ACCOUNT)