

from page_objects.base_page import BasePage
from locators.locators import MainPageLocators
import allure



class MainPage(BasePage):

    @allure.step('Переход в Конструктор')
    def click_on_constructor_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Переход на страницу Лента заказов')
    def click_on_order_list(self):
        self.click_element(MainPageLocators.ORDER_LIST_BUTTON)

    @allure.step('Кликнуть на ингредиент')
    def click_on_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT)

    @allure.step('Закрыть попап кнопкой крестик')
    def close_popup_button(self):
        self.click_element(MainPageLocators.CLOSE_POPUP_BUTTON)

    @allure.step('Добавить ингредиент в корзину заказа')
    def add_ingredient_in_order(self):
        self.drag_and_drop_on_element(MainPageLocators.INGREDIENT, MainPageLocators.ORDER_BASKET)

    @allure.step('Получить количество доьавленного в корзину ингредиента')
    def check_ingredient_counter(self):
        return self.get_actually_text(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Нажать на кнопку Оформить заказ')
    def click_make_order(self):
        self.click_element(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Сохранить номер заказа')
    def receive_order_number(self):
        self.wait_visibility_element(MainPageLocators.ORDER_ID_TEXT)
        self.wait_visibility_element(MainPageLocators.DEFAULT_ORDER)
        order_number = self.get_actually_text(MainPageLocators.ORDER_NUMBER)
        return order_number

    @allure.step('Закрыть попап заказа кнопкой крестик')
    def close_order_popup(self):
        self.wait_until_element_invisibility(MainPageLocators.COVER_ELEMENT)
        self.click_element(MainPageLocators.CLOSE_POPUP_BUTTON)








