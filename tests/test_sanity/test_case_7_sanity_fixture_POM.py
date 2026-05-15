from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.home_test_case_page import HomeTestCasePageObject


# Test Case 7: Verify Test Cases Page
def test_verify_test_cases_page(page: Page, base_url):
    homepage = HomePage(page,base_url)
    homepage.navigate_without_login()
    test_cases_validation = HomeTestCasePageObject(page)
    test_cases_validation.test_verify_test_cases_page_methods()
