import pytest

from pages.home import Homepage
from pages.login import loginpage
from pages.result import resultPage


@pytest.fixture
def  Homepageobj(page):
    Homepageobj=Homepage(page)
    return Homepageobj
@pytest.fixture
def  resultPageobj(page):
     resultPageobj=resultPage(page)
     return resultPageobj
@pytest.fixture
def laucnhingpage(page):  
    page.goto("https://amazon.in/")
@pytest.fixture
def loginpageobj(page):
    loginpageobj=loginpage(page)
    return loginpageobj
