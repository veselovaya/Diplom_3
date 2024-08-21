from page_objects.main_page import MainPage
from locators.locators import MainPageLocators, OrdersListLocators
from data import Urls
import allure


class TestMainOrder:
    @allure.title('Проверка перехода в Конструктор')
    def test_transfer_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_element(MainPageLocators.PERSONAL_ACCOUNT)
        main_page.wait_visibility_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        main_page.click_on_constructor_button()
        main_page.wait_visibility_element(MainPageLocators.CONSTRUCTOR_TITLE)
        assert main_page.find_element(MainPageLocators.CONSTRUCTOR_TITLE).text == 'Соберите бургер'

    @allure.title('Проверка перехода в Ленту заказов')
    def test_transfer_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_order_list()
        main_page.wait_visibility_element(OrdersListLocators.ORDER_LIST_TITLE)
        assert main_page.find_element(OrdersListLocators.ORDER_LIST_TITLE).text == 'Лента заказов'

    @allure.title('Проверка появления попапа с деталями при клике на ингредиент')
    def test_popup_with_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        assert main_page.find_element(MainPageLocators.INGREDIENT_POPUP).is_displayed()

    @allure.title('Проверка закрытия попапа с деталями ингредиента')
    def test_popup_ingredient_closed(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.wait_visibility_element(MainPageLocators.INGREDIENT_POPUP)
        main_page.close_popup_button()
        main_page.wait_until_element_invisibility(MainPageLocators.INGREDIENT_POPUP)
        assert main_page.find_element(MainPageLocators.INGREDIENT_POPUP).is_displayed() == False

    @allure.title('Проверка изменения каунтера ингредиента')
    def test_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        prev_counter = int(main_page.check_ingredient_counter())
        main_page.add_ingredient_in_order()
        now_counter = int(main_page.check_ingredient_counter())
        assert now_counter > prev_counter

    @allure.title('Проверка успешного создания заказа авторизованным пользователем')
    def test_authorized_user_make_order(self, driver,login):
        main_page = MainPage(driver)
        main_page.wait_visibility_element(MainPageLocators.INGREDIENT)
        main_page.add_ingredient_in_order()
        main_page.wait_for_element_to_be_clickable(MainPageLocators.MAKE_ORDER_BUTTON)
        main_page.click_make_order()
        main_page.wait_visibility_element(MainPageLocators.ORDER_NUMBER)
        assert main_page.find_element(MainPageLocators.ORDER_ID_TEXT).is_displayed()







