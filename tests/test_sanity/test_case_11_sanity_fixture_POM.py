from playwright.sync_api import Page
from pages.home_page import HomePage

# Test Case 11: Verify Subscription in Cart page


def test__Verify_Subscription_in_Cart_page(page: Page):
    homepage = HomePage(page)
    homepage.navigate_without_login()
    homepage.navigate_and_click_of_cart_link()
    homepage.Verify_soucription_in_home_page_method()
