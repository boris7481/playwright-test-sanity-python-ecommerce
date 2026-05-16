import pytest
from utils.ConfigReader import ReadConfig


@pytest.fixture(scope="session")
def base_url():
    return ReadConfig.get_property("BASE_URL")


@pytest.fixture
def fake_credentials():
    return {
        "email_fake": ReadConfig.get_property("email_fake"),
        "password_fake": ReadConfig.get_property("password_fake"),
    }


@pytest.fixture
def credentials_name_email():
    return {
        "name": ReadConfig.get_property("name"),
        "email": ReadConfig.get_property("email"),
    }


@pytest.fixture
def credentials_valid():
    return {
        "email": ReadConfig.get_property("email"),
        "password": ReadConfig.get_property("password"),
    }
