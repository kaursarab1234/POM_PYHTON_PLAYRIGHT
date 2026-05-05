from playwright.sync_api import Page,expect

class resultPage:
    def __init__(self,page:Page): 
        
        self.cartcount=page.locator("#nav-cart-count")
        self.addtocartbtn=lambda product: page.locator(f"//span[contains(text(), '{product}')]/ancestor::div[@class='a-section a-spacing-small a-spacing-top-small']//button[@aria-label='Add to cart']")
    def addtocart(self,itemname):
         self.addtocart(itemname).click()
    def cartcounttext(self):
         return self.cartcount.inner_text()    
