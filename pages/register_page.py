from faker import Faker

faker = Faker()
email = faker.email()


class RegisterPage:
    def __init__(self, page):
        self.page = page

    def account_informations(self):
        self.page.get_by_text("New User Signup!").is_visible()
        self.page.locator('[data-qa="signup-name"]').fill("09w0823@Freedom")
        self.page.locator('[data-qa="signup-email"]').fill(email)
        self.page.locator('[data-qa="signup-button"]').click()
        self.page.get_by_text("'ENTER ACCOUNT INFORMATION'").is_visible()
        self.page.get_by_role("radio", name="Mr.").check()
        self.page.get_by_label("Password").fill("Freedom95")
        self.page.locator('[data-qa="days"]').select_option("20")
        self.page.locator('[data-qa="months"]').select_option("10")
        self.page.locator('[data-qa="years"]').select_option("2000")
        self.page.get_by_label("Sign up for our newsletter!").check()
        self.page.get_by_label("Receive special offers from our partners!").check()
        self.page.get_by_label("First name").fill("Freedom95")
        self.page.get_by_label("Last name").fill("Freedom")
        self.page.locator("[data-qa='company']").fill("Freedom und co")
        self.page.locator("[data-qa='address']").fill("Bicler str 10")
        self.page.locator("[data-qa='address2']").fill("Bicler str 100")
        self.page.locator("[data-qa='country']").select_option("Canada")
        self.page.locator("[data-qa='state']").fill("Monreal")
        self.page.locator("[data-qa='city']").fill("regensburg")
        self.page.locator("[data-qa='zipcode']").fill("93051")
        self.page.locator("[data-qa='mobile_number']").fill("23774814615")
        self.page.locator("[data-qa='create-account']").click()
