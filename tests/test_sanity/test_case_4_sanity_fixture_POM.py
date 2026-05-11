import pytest
from playwright.sync_api import Page
import json
from pages.home_page import HomePage
from pages.login_page import LoginPage

with open("data/credentials.json") as file:
    test_data_valid = json.load(file)
    print(test_data_valid)
    user_credentials_valid_list = test_data_valid["valid_user_credentials"]


# user_credentials_valid or parameter ist the variable and user_credentials_valid_list is the itarable
@pytest.mark.smoke
@pytest.mark.parametrize("user_credentials_valid", user_credentials_valid_list)
def test_logout_user(page: Page, user_credentials_valid):
    user_name = user_credentials_valid["email"]
    password = user_credentials_valid["password"]

    logout_user = HomePage(page)
    logout_user.navigate_without_login()
    logout_user.selectordernavigationlink()

    login_page = LoginPage(page)  # object for loginPage class
    login_page.login(user_name, password)
    logout_user.logout_user_from_home_page()
