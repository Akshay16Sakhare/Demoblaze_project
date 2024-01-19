import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\Admin\PycharmProjects\Demo_Blaze_New\Configuration\config.ini")

class Read_values():

    @staticmethod
    def get_login_url():
        read_URL = config.get('info', 'login_url')
        return read_URL

    @staticmethod
    def get_username():
        read_username = config.get('info', 'username')
        return read_username

    @staticmethod
    def get_password():
        read_password = config.get('info', 'password')
        return read_password

    @staticmethod
    def get_Name_for_order():
        read_Name = config.get('place order', 'name')
        return read_Name

    @staticmethod
    def get_country():
        read_country = config.get('place order', 'country')
        return read_country

    @staticmethod
    def get_city():
        read_city = config.get('place order', 'city')
        return read_city

    @staticmethod
    def get_creditCard_No():
        read_creditCard_No = config.get('place order', 'creditcard')
        return read_creditCard_No

    @staticmethod
    def get_month():
        read_month = config.get('place order', 'month')
        return read_month

    @staticmethod
    def get_year():
        read_year = config.get('place order', 'year')
        return read_year