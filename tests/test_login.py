import json
import re
from playwright.sync_api import Page, expect


def test_example(page: Page,Homepageobj,loginpageobj) -> None:
   
    
    page.goto("https://www.amazon.in/")
    Homepageobj.accountandlistclick()
    with open("testData/credentials.json") as f:
        data=json.load(f)
        print(data)
    #page.get_by_role("link", name="Sign in", exact=True).click()
    loginpageobj.enteremail(data["positivecrdentials"]["username"])
    loginpageobj.clickcontinue()
    loginpageobj.enterpassword(data["positivecrdentials"]["password"])
    loginpageobj.clicksignin()
  
   
    expect(page.get_by_role("searchbox", name="Search Amazon.in")).to_be_visible()


