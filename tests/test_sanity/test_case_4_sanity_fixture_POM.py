import pytest
from playwright.sync_api import Page
import json
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.DataProviders import resd_json_file
from pathlib import Path

#with open("TestData/credentials.json") as file:
#    test_data_valid = json.load(file)
#    print(test_data_valid)
#    user_credentials_valid_list = test_data_valid["valid_user_credentials"]


path_json_credential = Path(__file__).resolve().parent.parent.parent / "TestData" / 'credentials.json'

credentials_data = resd_json_file(path_json_credential)

# user_credentials_valid or parameter ist the variable and user_credentials_valid_list is the itarable
@pytest.mark.smoke
@pytest.mark.parametrize("user_credentials_valid", credentials_data["valid_user_credentials"])
def test_logout_user(page: Page,base_url, user_credentials_valid):
    user_name = user_credentials_valid["email"]
    password = user_credentials_valid["password"]

    logout_user = HomePage(page, base_url)
    logout_user.navigate_without_login()
    logout_user.selectordernavigationlink()

    login_page = LoginPage(page)  # object for loginPage class
    login_page.login(user_name, password)
    logout_user.logout_user_from_home_page()
