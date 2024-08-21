from page_objects.order_feed_page import OrderFeed
from locators.locators import OrdersListLocators, MainPageLocators, PersonalAccountLocators
from page_objects.main_page import MainPage
from page_objects.personal_acc_page import PersonalAccountPage
import allure


class TestOrderFeed:

    @allure.title('Проверка открытия попапа с деталями заказа')
    def test_open_details_order_popup(self, driver):
        feed_page = OrderFeed(driver)
        feed_page.click_element(MainPageLocators.ORDER_LIST_BUTTON)
        feed_page.wait_visibility_element(OrdersListLocators.ORDER_LIST_TITLE)
        feed_page.check_order_details()
        feed_page.wait_visibility_element(OrdersListLocators.ORDER_DETAILS_POPUP)
        assert feed_page.find_element(OrdersListLocators.ORDER_DETAILS_POPUP).is_displayed()

    @allure.title('Проверка отображения созданного заказа в Ленте заказов и в ЛК')
    def test_order_number_from_account_in_total_list(self, driver, login):
        main_page = MainPage(driver)
        main_page.wait_visibility_element(MainPageLocators.INGREDIENT)
        main_page.add_ingredient_in_order()
        main_page.click_make_order()
        main_page.wait_visibility_element(MainPageLocators.DEFAULT_ORDER)
        main_page.wait_visibility_element(MainPageLocators.ORDER_ID_TEXT)
        main_page.close_order_popup()
        acc_page = PersonalAccountPage(driver)
        acc_page.click_pers_acc_button_on_main()
        acc_page.wait_visibility_element(PersonalAccountLocators.PROFILE_HEADER)
        acc_page.click_order_list()
        acc_page.wait_visibility_element(PersonalAccountLocators.ORDER_NUMBER_IN_ACCOUNT)
        order = acc_page.check_order_number_in_account()
        main_page.click_on_order_list()
        feed_page = OrderFeed(driver)
        feed_page.wait_visibility_element(OrdersListLocators.ORDER_LIST_TITLE)
        order_in_list = feed_page.find_numbers_order(order)
        assert order in order_in_list

    @allure.title('Проверка увеличения счетчика заказов за все время после создания заказа')
    def test_counter_total_increase(self,driver,login):
        main_page = MainPage(driver)
        feed_page = OrderFeed(driver)
        main_page.click_on_order_list()
        feed_page.wait_visibility_element(OrdersListLocators.ORDER_LIST_TITLE)
        total_1 = feed_page.get_total_orders()
        main_page.click_on_constructor_button()
        main_page.wait_visibility_element(MainPageLocators.CONSTRUCTOR_TITLE)
        main_page.add_ingredient_in_order()
        main_page.click_make_order()
        main_page.wait_visibility_element(MainPageLocators.DEFAULT_ORDER)
        main_page.wait_visibility_element(MainPageLocators.ORDER_ID_TEXT)
        main_page.close_order_popup()
        main_page.click_on_order_list()
        main_page.wait_visibility_element(OrdersListLocators.ORDER_LIST_TITLE)
        total_2 = feed_page.get_total_orders()
        assert total_2 > total_1

    @allure.title('Проверка увеличения счетчика заказов за сегодня после создания заказа')
    def test_counter_today_increase(self, driver, login):
        main_page = MainPage(driver)
        feed_page = OrderFeed(driver)
        main_page.click_on_order_list()
        feed_page.wait_visibility_element(OrdersListLocators.ORDER_LIST_TITLE)
        total_1 = feed_page.get_orders_for_today()
        main_page.click_on_constructor_button()
        main_page.wait_visibility_element(MainPageLocators.CONSTRUCTOR_TITLE)
        main_page.add_ingredient_in_order()
        main_page.click_make_order()
        main_page.wait_visibility_element(MainPageLocators.DEFAULT_ORDER)
        main_page.wait_visibility_element(MainPageLocators.ORDER_ID_TEXT)
        main_page.close_order_popup()
        main_page.click_on_order_list()
        main_page.wait_visibility_element(OrdersListLocators.ORDER_LIST_TITLE)
        total_2 = feed_page.get_orders_for_today()
        assert total_2 > total_1

    @allure.title('Проверка, есть ли созданный заказ среди заказов в работе')
    def test_order_is_in_progress_list(self, driver, login):
        main_page = MainPage(driver)
        feed_page = OrderFeed(driver)
        main_page.wait_visibility_element(MainPageLocators.CONSTRUCTOR_TITLE)
        main_page.add_ingredient_in_order()
        main_page.click_make_order()
        main_page.wait_until_element_invisibility(MainPageLocators.DEFAULT_ORDER)
        main_page.wait_visibility_element(MainPageLocators.ORDER_ID_TEXT)
        my_order = main_page.get_actually_text(MainPageLocators.ORDER_NUMBER)
        main_page.close_order_popup()
        main_page.click_on_order_list()
        orders_in_progress = feed_page.check_order_number_in_progress()
        assert my_order in orders_in_progress
































