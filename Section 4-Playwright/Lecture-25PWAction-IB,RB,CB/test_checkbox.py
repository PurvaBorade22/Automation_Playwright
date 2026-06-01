import pytest
from playwright.sync_api import Page, expect

def test_checkbox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    
    # 1) checked a single checkbox
    # sunday_checkbox = page.get_by_label("Sunday")
    # sunday_checkbox.check()
    # expect(sunday_checkbox).to_be_checked()
    # page.wait_for_timeout(5000)
    
     #2. count number of check boxes
    days= ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    checkboxes=[]
    
    # for day in days:
    #     checkbox = page.get_by_label(day)
    #     checkboxs.append(checkbox)
        
    # in simple syntax 
    
    checkboxes=[page.get_by_label(day) for day in days]
    print("Total number of checkbox:",len(checkboxes))
    
    # 3) selecting all the checkbox
    for checkbox in checkboxes:
        checkbox.check()
        expect(checkbox).to_be_checked()
        page.wait_for_timeout(5000)    
        