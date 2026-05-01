from playwright.sync_api import expect
import os
from faker import Faker

faker = Faker()
email = faker.email()


class AddressDetailsandReview:

    def __init__(self, page):
        self.page = page

    def Address_Details_and_Review(self):
        expect(self.page.get_by_text("Address Details")).to_be_visible()
        expect(self.page.get_by_text("Review Your Order")).to_be_visible()
        self.page.locator(".form-control").fill("everything is op")
        self.page.get_by_role("link", name="Place Order").click()
        self.page.locator("[data-qa='name-on-card']").fill("Master Card")
        self.page.locator("[data-qa='card-number']").fill("10-2-30")
        self.page.locator("[data-qa='cvc']").fill("200")
        self.page.locator("[data-qa='expiry-month']").fill("10-02-30")
        self.page.locator("[data-qa='expiry-year']").fill("2030")
        self.page.locator("[data-qa='pay-button']").click()
        expect(
            self.page.get_by_text("Congratulations! Your order has been confirmed!")
        ).to_be_visible()
        self.page.locator("[data-qa='continue-button']").click()

    def downlaod_invoices(self):
        with self.page.expect_download() as download_info:
            self.page.get_by_role("link", name="Download Invoice").click()

        download = download_info.value

        # Sauvegarde
        file_path = f"./downloads/{download.suggested_filename}"
        download.save_as(file_path)

        # Vérifications
        assert os.path.exists(file_path)
        assert os.path.getsize(file_path) > 0  # --> to check the size
        assert "invoice" in download.suggested_filename.lower()

        self.page.locator("[data-qa='continue-button']").click()
