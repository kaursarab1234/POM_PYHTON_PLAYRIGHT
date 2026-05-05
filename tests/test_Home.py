from playwright.sync_api import sync_playwright,expect
from pages.home import Homepage
import pytest
searchbox="//input[@id='twotabsearchtextbox']"

@pytest.mark.test

def test_validatingTheHomeOfHomeScreen(self,page):
    #with sync_playwright() as p:
       #B= p.chromium.launch(headless=False)
       #P=B.new_context()
       #page.new_page
       Homepageobj=Homepage(page)
       Homepageobj.visibilityofsearchbox()
       page.goto("https://amazon.in/")
       page.wait_for_selector("#twotabsearchtextbox",state='visible')
       expect(page.get_by_placeholder("Search Amazon.in")).to_be_visible()
       self.accountandlist=page.get_by_text("Account & Lists ")

#test_validatingTheHomeOfHomeScreen() 

@pytest.mark.test
def test_validatingCarticon(page):
    page.goto("https://amazon.in/")
    Homepageobj=Homepage(page)
    Homepageobj.visibilityofsearchbox()
    expect(page.get_by_test_id('nav-cart-text-container')).to_be_visible()

def visiblitiyofsearchbar(self):
    self.searchbox.wait_for(State='visible')

def accountandvisibility(self):
    expect(self.accountandlist).to_be_visible()
def entersearchtest(self,product):
   self.searchbox(product)
def validatevisibilityofcarticon(self,page):
   expect(page.get_by_test_id('nav-cart-text-container')).to_be_visible()




    

 
