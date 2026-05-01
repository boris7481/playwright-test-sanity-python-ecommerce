from playwright.sync_api import expect


class CartPage:
    def __init__(self, page):
        self.page = page

    def check_the_product_in_cart(self):
        expect(self.page.get_by_text("Blue Top").first).to_be_visible()
        expect(self.page.get_by_text("Men Tshirt").first).to_be_visible()

    def go_to_art_page_Verify_that_those_products_are_visible_in_cart_after_login_aswell(
        self,
    ):
        self.page.get_by_role("link", name="Cart").click()
        expect(self.page.get_by_text("Premium Polo T-Shirts")).to_be_visible()

    def Click_Proceed_To_Checkout(self):
        self.page.get_by_text("Proceed To Checkout").click()

    def Click_Proceed_To_Checkout_and_register(self):
        self.page.get_by_role("link", name="Register / Login").click()

    def Place_to_checkout_and_check_the_adrees(self):
        self.page.get_by_role("link", name="Cart").click()
        self.page.get_by_text("Proceed To Checkout").click()
        expect(self.page.get_by_text("Address Details")).to_be_visible()
        expect(self.page.locator(".address_delivery = .address_invoice"))
