from data import Urls
from locators.locators import RestorePasswordLocators, MainPageLocators
from page_objects.restore_password_page import RestorePasswordPage
import allure

class TestRestorePassword:

    @allure.title('Проверка перехода по клику на Восстановить пароль на странице авторизации')
    def test_click_restore_link_on_main(self, driver):
        restore_page = RestorePasswordPage(driver)
        restore_page.click_element(MainPageLocators.LOGIN_ON_MAIN_BUTTON)
        restore_page.click_on_restore_password_link()
        restore_page.wait_visibility_element(RestorePasswordLocators.RESTORE_PASSWRD_BUTTON)
        forgot_url = restore_page.current_url()
        assert forgot_url == (Urls.FORGOT_PASS)

    @allure.title('Проверка перехода по кнопке Восстановить после ввода емейла')
    def test_fill_email_click_restore(self, driver):
        restore_page = RestorePasswordPage(driver)
        restore_page.open_site_link(Urls.RESTORE_PASS)
        restore_page.wait_visibility_element(RestorePasswordLocators.RESTORE_PASSWRD_BUTTON)
        restore_page.fill_in_email_for_restore()
        restore_page.click_on_restore_button()
        restore_page.wait_visibility_element(RestorePasswordLocators.INPUT_PASSWORD_FOR_RESTORE)
        restore_url = restore_page.current_url()
        assert  restore_url == (Urls.RESTORE_PASS)

    @allure.title('Проверка, что поле Пароль активно после нажатия на кнопку Показать/скрыть пароль')
    def test_click_show_pass_input_active(self, driver):
        restore_page = RestorePasswordPage(driver)
        restore_page.open_site_link(Urls.FORGOT_PASS)
        restore_page.wait_visibility_element(RestorePasswordLocators.RESTORE_PASSWRD_BUTTON)
        restore_page.fill_in_email_for_restore()
        restore_page.click_on_restore_button()
        restore_page.wait_visibility_element(RestorePasswordLocators.INPUT_PASSWORD_FOR_RESTORE)
        restore_page.fill_in_password_for_restore()
        restore_page.click_show_password()
        restore_page.wait_visibility_element(RestorePasswordLocators.ACTIVE_PASSWORD_INPUT)
        element = restore_page.find_password_active()
        assert element.is_displayed()

