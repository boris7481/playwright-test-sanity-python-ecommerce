from playwright.sync_api import Page
from pages.home_page import HomePage

# Test Case 10: Verify Subscription in home page


def test_verify_subscription_in_home_page(page: Page):
    homepage = HomePage(page)
    homepage.navigate_without_login()
    homepage.verify_soucription_in_home_page_method()
