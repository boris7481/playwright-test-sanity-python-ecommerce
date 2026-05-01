import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def go_to_page_einwilligen(page: Page):
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="Einwilligen").click()
    return page


@pytest.fixture
def go_to_page_login(page: Page):
    page.goto("https://www.automationexercise.com/")
    expect(page.get_by_text("Video Tutorials")).to_be_visible()
    page.get_by_role("button", name="Einwilligen").click()
    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_text("Login to your account")).to_be_visible()
    return page


# request in bracket help us to access your global environment variable
# as well as your local pytest foction variable
# Globla variable (for example to control in which browser your test should run)
# the param here refert to user_credentials_valid in the bracket of the function
# scope = session : the fixture will be execute once before full execution of the test beginn
@pytest.fixture(scope="session")
def user_credentials_valid(request):
    return request.param


@pytest.fixture
def fake_credentials():
    return {
        "email_fake": "flase@gmail.com",
        "password_fake": "Freedom95_fake",
    }


@pytest.fixture
def credentials_name_email():
    return {
        "name": "09w0823@Freedom",
        "email": "freedomvision@gmail.com",
    }


@pytest.fixture
def credentials_valid():
    return {
        "email": "freedomvision@gmail.com",
        "password": "Freedom95",
    }
