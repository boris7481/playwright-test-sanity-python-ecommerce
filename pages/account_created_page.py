from playwright.sync_api import expect


class AccountCreatedPage:

    def __init__(self, page):
        self.page = page

    def account_created(self):
        expect(self.page.get_by_text("ACCOUNT CREATED!")).to_be_visible()
        self.page.locator("[data-qa='continue-button']").click()
