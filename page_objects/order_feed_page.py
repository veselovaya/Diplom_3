from page_objects.base_page import BasePage
from locators.locators import MainPageLocators, OrdersListLocators
import allure


class OrderFeed(BasePage):

    @allure.step('Открыть детали заказа в списке Ленты Заказов')
    def check_order_details(self):
        self.click_element(OrdersListLocators.ORDER_CARD)

    @allure.step('Найти заказ по номеру в Ленте заказов')
    def find_numbers_order(self, order):
        path = OrdersListLocators.ORDER_NUMBER_IN_LIST[0]
        locator = OrdersListLocators.ORDER_NUMBER_IN_LIST[1]
        locator = locator.format(order)
        return self.get_actually_text((path, locator))

    @allure.step('Найти заказ по номеру среди заказов в работе')
    def check_order_number_in_progress(self):
        self.wait_visibility_element(OrdersListLocators.READY_ORDERS_TEXT)
        self.wait_until_element_invisibility(OrdersListLocators.READY_ORDERS_TEXT)
        return self.get_actually_text(OrdersListLocators.ORDER_IN_PROGRESS)

    @allure.step('Получить общее количество заказов, выполненных за все время')
    def get_total_orders(self):
        return self.get_actually_text(OrdersListLocators.TOTAL_ORDERS)

    @allure.step('Получить общее количество заказов, выполненных за сегодня')
    def get_orders_for_today(self):
        return self.get_actually_text(OrdersListLocators.TODAY_ORDERS)

