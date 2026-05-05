from playwright.sync_api import Page,expect
import pytest
from pages.home import Homepage
from pages.result import resultPage

    
    




@pytest.mark.resultpage
def test_validatingcarticon(page:Page,Homepageobj,resultPageobj):
    
    Homepageobj.entersearchtest("i phone 17")
    
    page.wait_for_timeout(30000)
    Homepageobj.clickonsearchbtn()
    resultPageobj.addtocart("i phone 17")
    beforeadding=resultPageobj.cartcounttext()
    page.wait_for_timeout(30000)
    afteradding=resultPageobj.cartcounttext()
    assert(int(afteradding)>int(beforeadding)) 