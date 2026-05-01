class LoginPage:

    def __init__(self, page):
        self.page = page

    def login(self, email, password):
        self.page.locator('[data-qa="login-email"]').fill(email)
        self.page.locator('[data-qa="login-password"]').fill(password)
        self.page.locator('[data-qa="login-button"]').click()

    def signup(self, user_name, email):
        self.page.locator('[data-qa="signup-name"]').fill(user_name)
        self.page.locator('[data-qa="signup-email"]').fill(email)
        self.page.locator('[data-qa="signup-button"]').click()
