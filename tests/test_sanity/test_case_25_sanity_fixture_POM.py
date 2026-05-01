from playwright.sync_api import Page
from pages.home_page import HomePage

# Test Case 25: Verify Scroll Up using 'Arrow' button and Scroll Down functionality


def test_Verify_Scroll_Up_using_Arrow_button_and_Scroll_Down_functionality(page: Page):
    homepage = HomePage(page)
    homepage.navigate_without_login()
    homepage.scroll_up_and_down()
