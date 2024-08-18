from faker import Faker

class Urls:
    URL = 'https://stellarburgers.nomoreparties.site/'
    LOGIN = 'https://stellarburgers.nomoreparties.site/login'
    FORGOT_PASS = 'https://stellarburgers.nomoreparties.site/forgot-password'
    RESTORE_PASS = 'https://stellarburgers.nomoreparties.site/reset-password'
    CREATE_USER = 'api/auth/register'
    DELETE_USER = 'api/auth/user'
    PERSONAL_ACCOUNT = 'https://stellarburgers.nomoreparties.site/account/profile'
    ORDER_LIST = 'https://stellarburgers.nomoreparties.site/account/order-history'


class UserData:
    @staticmethod
    def create_user_data():
        fake = Faker()
        user_data = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()
        }
        return user_data

