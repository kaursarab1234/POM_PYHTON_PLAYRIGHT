from playwright.sync_api import Page,expect

class Homepage:
    def __init__(self,page:Page):
        self.searchbtn=page.get_by_test_id("nav-search-submit-button")
       


    def visiblitiyofsearchbar(self):
       self.searchbox.wait_for(State='visible')

    def accountandvisibility(self):
        expect(self.accountandlist).to_be_visible()
    def entersearchtest(self,product):
        self.searchbox.wait_for(State='visible')
        self.searchbox.fill(product)
    def validatevisibilityofcarticon(self,page):
        expect(page.get_by_test_id('nav-cart-text-container')).to_be_visible()
    def clickonsearchbtn(self):
        self.searchbtn.click()

