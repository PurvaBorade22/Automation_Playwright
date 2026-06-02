import pytest

from playwright.sync_api import Page, expect

def test_excercise(page:Page):
    page.goto("https://practice-automation.com/form-fields/")
    
    # 1) Name input field
    name_textbox = page.locator("#name-input")
    expect(name_textbox).to_be_visible()
    expect(name_textbox).to_be_enabled()
    name_textbox.fill("Purva Borade")
    getenteredvalue = name_textbox.input_value()
    print("Entered value is:", getenteredvalue)
    
    # 2) password input filed
    password = page.locator("input[type='password']")
    expect(password).to_be_visible()
    expect(password).to_be_enabled()
    password.fill("Purva@123")
    getenteredvalue = password.input_value()
    print("Entered value is:", getenteredvalue)
    
    # 3) radio button
    yellow_color = page.locator("#color3")
    expect(yellow_color).to_be_visible()
    expect(yellow_color).to_be_enabled()
    expect(yellow_color).not_to_be_checked()
    yellow_color.check()
    expect(yellow_color).to_be_checked()
    
    # 4) Checkbox
    #method 1
    coffee_checkbox = page.locator("#drink3")
    coffee_checkbox.check()
    expect(coffee_checkbox).to_be_checked()
    
    #method 2 how many label of checkboxes
    drinks =['Water','Milk','Coffee','Wine','Ctrl-Alt-Delight']    
    checkboxes=[]
    
    checkboxes=[page.get_by_label(drink) for drink in drinks]
    print("Total number of checkboxes:",len(checkboxes))
    
    #method 3
    for checkbox in checkboxes:
        checkbox.check()
        expect(checkbox).to_be_checked()
        
    #method 4 by indexing select checkbox
    for checkbox in checkboxes[1:3]:
        checkbox.uncheck()
        expect(checkbox).not_to_be_checked()
    
    page.wait_for_timeout(5000)