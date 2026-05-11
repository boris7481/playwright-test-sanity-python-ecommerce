import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.login_page import LoginPage

# Test Case 5: Register User with existing email


@pytest.mark.smoke
def test_register_user_with_existing_emai(page: Page, credentials_name_email):
    user_name = credentials_name_email["name"]
    email = credentials_name_email["email"]
    homepage = HomePage(page)
    homepage.navigate_without_login()
    homepage.selectordernavigationlink_signup()

    sigu_page = LoginPage(page)  # object for loginPage class
    sigu_page.signup(user_name, email)
    expect(page.get_by_text("Email Address already exist")).to_be_visible()
