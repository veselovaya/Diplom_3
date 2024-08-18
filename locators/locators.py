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




