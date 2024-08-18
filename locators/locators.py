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

class PersonalAccountLocators:
    ORDERS_LIST_LINK = (By.XPATH, '//a[text()="История заказов"]') #гиперссылка "История заказов"
    EXIT_LINK = (By.XPATH, '//button[text() = "Выход"]')  # гиперссылка ""Выход"
    LOGIN_INPUT_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # инпут ввода емейла для логина
    LOGIN_INPUT_PASSWORD = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')  # инпут ввода пароля для логина
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]')  # кнопка "Войти" на отдельной странице
    PROFILE_HEADER = (By.XPATH, '//a[text()="Профиль"]')  # заголовок "Профиль" на странице личного кабинета








