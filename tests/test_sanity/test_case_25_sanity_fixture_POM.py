from playwright.sync_api import Page
from pages.home_page import HomePage

# Test Case 25: Verify Scroll Up using 'Arrow' button and Scroll Down functionality


def test_verify_scroll_up_using_arrow_button_and_scroll_down_functionality(page: Page):
    homepage = HomePage(page)
    homepage.navigate_without_login()
    homepage.scroll_up_and_down()
