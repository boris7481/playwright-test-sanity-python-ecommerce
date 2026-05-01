from playwright.sync_api import Page
from pages.home_page import HomePage

# Test Case 10: Verify Subscription in home page


def test_Verify_Subscription_in_home_page(page: Page):
    homepage = HomePage(page)
    homepage.navigate_without_login()
    homepage.Verify_soucription_in_home_page_method()
