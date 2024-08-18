from page_objects.personal_acc_page import PersonalAccountPage
from locators.locators import MainPageLocators, PersonalAccountLocators
from data import Urls


class TestPersonalAccount:

    def test_transfer_to_personal_acc(self, driver, login):
        acc_page = PersonalAccountPage(driver)
        acc_page.wait_visibility_element(MainPageLocators.PERSONAL_ACCOUNT)
        acc_page.click_profile_settings()
        acc_page.wait_visibility_element(PersonalAccountLocators.PROFILE_HEADER)
        now_page = acc_page.current_url()
        assert now_page == (Urls.PERSONAL_ACCOUNT)


    def test_transfer_to_order_list(self, driver, login):
        acc_page = PersonalAccountPage(driver)
        acc_page.wait_visibility_element(MainPageLocators.PERSONAL_ACCOUNT)
        acc_page.click_profile_settings()
        acc_page.wait_visibility_element(PersonalAccountLocators.ORDERS_LIST_LINK)
        acc_page.click_order_list()
        now_page = acc_page.current_url()
        assert now_page == (Urls.ORDER_LIST)


    def test_logout_user(self, driver, login):
        acc_page = PersonalAccountPage(driver)
        acc_page.wait_visibility_element(MainPageLocators.PERSONAL_ACCOUNT)
        acc_page.click_profile_settings()
        acc_page.wait_visibility_element(PersonalAccountLocators.EXIT_LINK)
        acc_page.click_exit_link()
        acc_page.wait_visibility_element(PersonalAccountLocators.LOGIN_BUTTON)
        assert acc_page.find_element(PersonalAccountLocators.LOGIN_BUTTON).text == 'Войти'




