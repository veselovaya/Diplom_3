from selenium.webdriver.common.by import By


class RestorePasswordLocators:
    RESTORE_PASSWRD_HYPERLINK = (By.XPATH, '//a[@href = "/forgot-password"]') #гиперссылка "Восстановить пароль"
    INPUT_EMAIL_FOR_RESTORE = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # инпут ввода емейла для восстановления
    RESTORE_PASSWRD_BUTTON = (By.XPATH, '//button[text()="Восстановить"]') #кнопка "Восстановить" на странице Восстановления пароя
    INPUT_PASSWORD_FOR_RESTORE = (By.XPATH, '//input[@type="password"]') #инпут ввода  пароля на странице Восстановление пароля
    SAVE_BUTTON_FOR_RESTORE = (By.XPATH, '//button[text()="Сохранить"]') #кнопка "Сохранить" на странице Восстановление пароля
    SHOW_PASSWORD_ICON = (By.XPATH, '//div[contains(@class,"icon-action")]') #кнопка "показать/скрыть пароль"
    ACTIVE_PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, "input_status_active")]') #инпут пароля активен

class MainPageLocators:
    LOGIN_ON_MAIN_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # кнопка "Войти в аккаунт" на главной
    PERSONAL_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]')  # кнопка "Личный Кабинет" в хэдере
    ORDER_LIST_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a')  # кнопка "Лента Заказов" в хэдере
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]/parent::a') # кнопка "Конструктор" в хэдере
    CONSTRUCTOR_TITLE = By.XPATH, '//h1[text()="Соберите бургер"]'  # заголовок "Соберите бургер"
    INGREDIENT = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]') # ингредиент "Булка"
    INGREDIENT_POPUP = (By.XPATH, '//h2[text()="Детали ингредиента"]')  # Детали ингредиента
    CLOSE_POPUP_BUTTON = (By.XPATH, '//button[contains(@class, "Modal_modal__close_modified")]') # Крестик закрытия попапа
    INGREDIENT_COUNTER = (By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]')  # Каунтер ингредиента
    ORDER_BASKET = By.XPATH, '//ul[contains(@class,"basket")]'  # Корзина
    MAKE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'  # кнопка "Оформить заказ"
    ORDER_ID_TEXT = (By.XPATH, '//p[text()="идентификатор заказа"]')  # Идентификатор заказа
    ORDER_NUMBER = By.XPATH, '//*[contains(@class, "type_digits-large")]'  # номер заказа в попапе
    DEFAULT_ORDER = By.XPATH, '//h2[text()="9999"]'  # дефолтный номер заказа в попапе
    COVER_ELEMENT = (By.XPATH, "//*[contains(@class, 'Modal_modal__loading')]"
                               "/following::div[@class='Modal_modal_overlay__x2ZCr']") # перекрывающий элемент






class PersonalAccountLocators:
    ORDERS_LIST_LINK = (By.XPATH, '//a[text()="История заказов"]') #гиперссылка "История заказов"
    EXIT_LINK = (By.XPATH, '//button[text() = "Выход"]')  # гиперссылка ""Выход"
    LOGIN_INPUT_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # инпут ввода емейла для логина
    LOGIN_INPUT_PASSWORD = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')  # инпут ввода пароля для логина
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]')  # кнопка "Войти" на отдельной странице
    PROFILE_HEADER = (By.XPATH, '//a[text()="Профиль"]')  # заголовок "Профиль" на странице личного кабинета
    ORDER_NUMBER_IN_ACCOUNT = (By.XPATH, '//*[contains(@class,"textBox")]//p[contains(@class,"digits-default")]') # номер заказа в личном кабинете



class OrdersListLocators:
    TOTAL_ORDERS = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class,"digits-large")]')   # количество  заказов за все время
    TODAY_ORDERS = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,"digits-large")]') # количество  заказов за сегодня
    READY_ORDERS_TEXT = (By.XPATH, '//li[text()="Все текущие заказы готовы!"]') # напдись "Все теущие заказы готовы"
    COUNTER_TOTAL_ORDERS = [By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p'] # счетчик заказов за все время
    COUNTER_TODAY_ORDERS = [By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p'] # счетчик заказов за сегодня
    ORDER_LIST_TITLE = By.XPATH, '//h1[text()="Лента заказов"]'  # Заголовок Лента заказов
    ORDER_CARD = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")]') # карточка Заказа
    ORDER_NUMBER_IN_LIST = By.XPATH, '//p[text()="{}"]'  # номер заказа из Ленты заказов
    ORDER_IN_PROGRESS = (By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]')  # номер заказа в работе
    ORDER_DETAILS_POPUP = (By.XPATH, '//p[text()="Cостав"]') # надпись "Состав" в попапе деталей заказа
























