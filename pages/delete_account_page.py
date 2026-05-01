from playwright.sync_api import expect


class DeletePage:

    def __init__(self, page):
        self.page = page

    def delete_account(self):
        expect(self.page.get_by_text("ACCOUNT DELETED!")).to_be_visible()
