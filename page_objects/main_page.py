from page_objects.base_page import BasePage
from locators.locators import MainPageLocators



class MainPage(BasePage):

    def click_on_constructor_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_on_order_list(self):
        self.click_element(MainPageLocators.ORDER_LIST_BUTTON)

    def click_on_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT)

    def close_popup_button(self):
        self.click_element(MainPageLocators.CLOSE_POPUP_BUTTON)


    def add_ingredient_in_order(self):
        self.drag_and_drop_on_element(MainPageLocators.INGREDIENT, MainPageLocators.ORDER_BASKET)

    def check_ingredient_counter(self):
        return self.get_actually_text(MainPageLocators.INGREDIENT_COUNTER)

    def click_make_order(self):
        self.click_element(MainPageLocators.MAKE_ORDER_BUTTON)

    def receive_order_number(self):
        self.wait_visibility_element(MainPageLocators.ORDER_ID_TEXT)
        self.wait_visibility_element(MainPageLocators.DEFAULT_ORDER)
        order_number = self.get_actually_text(MainPageLocators.ORDER_NUMBER)
        return order_number







