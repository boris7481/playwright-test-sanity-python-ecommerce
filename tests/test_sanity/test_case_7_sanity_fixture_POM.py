from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.home_test_case_page import HomeTestCasePageObject


# Test Case 7: Verify Test Cases Page
def test_Verify_Test_Cases_Page(page: Page):
    homepage = HomePage(page)
    homepage.navigate_without_login()
    test_cases_validation = HomeTestCasePageObject(page)
    test_cases_validation.test_Verify_Test_Cases_Page_methods()
