# Test Case 26: Verify Scroll Up without 'Arrow' button and Scroll Down functionality

from playwright.sync_api import Page
from pages.home_page import HomePage


def test_verify_scroll_up_using_arrow_button_and_scroll_down_unctionality(page: Page,base_url):
    homepage = HomePage(page,base_url)
    homepage.navigate_without_login()
    homepage.scroll_up_and_down_and_wait_arrow()