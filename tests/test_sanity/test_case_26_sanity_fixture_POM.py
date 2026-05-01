# Test Case 26: Verify Scroll Up without 'Arrow' button and Scroll Down functionality

from playwright.sync_api import Page
from pages.home_page import HomePage


def test_Verify_Scroll_Up_using_Arrow_button_and_Scroll_Down_unctionality(page: Page):
    homepage = HomePage(page)
    homepage.navigate_without_login()
    homepage.scroll_up_and_down_and_wait_arrow()
