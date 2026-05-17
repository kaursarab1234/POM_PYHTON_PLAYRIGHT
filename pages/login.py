from playwright.sync_api import Page,expect
class loginpage:
    def __init__(self,page:Page):
        self.emailtextbox=page.get_by_role("textbox", name="Enter mobile number or email")
        self.continuebutton=page.locator("//input[@type='submit']")
        self.passwordtextbox=page.get_by_role("textbox", name="Password")
        self.signinbutton=page.get_by_role("button", name="Sign in")
    
    def enteremail(self,email):
        self.emailtextbox.click()
        self.emailtextbox.fill(email)
    def clickcontinue(self):
        self.continuebutton.click()
    def enterpassword(self,password):
        self.passwordtextbox.click()
        self.passwordtextbox.fill(password)
    def clicksignin(self):
        self.signinbutton.click()