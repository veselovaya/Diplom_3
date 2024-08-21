from page_objects.base_page import BasePage
from locators.locators import RestorePasswordLocators
import allure


class RestorePasswordPage(BasePage):

    @allure.step('Нажать на Восстановить пароль')
    def click_on_restore_password_link(self):
        self.click_element(RestorePasswordLocators.RESTORE_PASSWRD_HYPERLINK)

    @allure.step('Ввести емейл  для восстановления пароля')
    def fill_in_email_for_restore(self):
        self.send_keys(RestorePasswordLocators.INPUT_EMAIL_FOR_RESTORE, 'nastya_veselova_10133@ya.ru')

    @allure.step('Нажать на кнопку Восстановить')
    def click_on_restore_button(self):
        self.click_element(RestorePasswordLocators.RESTORE_PASSWRD_BUTTON)

    @allure.step('Нажать на кнопку Показать/скрыть пароль')
    def click_show_password(self):
        self.click_element(RestorePasswordLocators.SHOW_PASSWORD_ICON)

    @allure.step('Найти активное поле Пароль')
    def find_password_active(self):
        return self.find_element(RestorePasswordLocators.ACTIVE_PASSWORD_INPUT)

    @allure.step('Ввести новый пароль для восстановления УЗ')
    def fill_in_password_for_restore(self):
        self.send_keys(RestorePasswordLocators.INPUT_PASSWORD_FOR_RESTORE, '1234567')






