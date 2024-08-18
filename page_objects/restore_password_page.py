from page_objects.base_page import BasePage
from locators.locators import RestorePasswordLocators


class RestorePasswordPage(BasePage):

    def click_on_restore_password_link(self):
        self.click_element(RestorePasswordLocators.RESTORE_PASSWRD_HYPERLINK)

    def fill_in_email_for_restore(self):
        self.send_keys(RestorePasswordLocators.INPUT_EMAIL_FOR_RESTORE, 'nastya_veselova_10133@ya.ru')

    def click_on_restore_button(self):
        self.click_element(RestorePasswordLocators.RESTORE_PASSWRD_BUTTON)

    def click_show_password(self):
        self.click_element(RestorePasswordLocators.SHOW_PASSWORD_ICON)

    def find_password_active(self):
        return self.find_element(RestorePasswordLocators.ACTIVE_PASSWORD_INPUT)

    def fill_in_password_for_restore(self):
        self.send_keys(RestorePasswordLocators.INPUT_PASSWORD_FOR_RESTORE, '1234567')






