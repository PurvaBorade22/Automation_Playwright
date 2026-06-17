import pytest

from playwright.sync_api import Page,expect

def select_date(page,target_year,target_month,target_date,is_future):
    while True:
        current_month = page.locator(".ui-datepicker-month").text_content()
        current_year = page.locator(".ui-datepicker-year").text_content()

        if current_month == target_month and current_year == target_year:
            break
        if is_future == True:
            page.locator(".ui-datepicker-next").click()
        else:
            page.locator(".ui-datepicker-prev").click()

    all_dates=page.locator(".ui-datepicker-calendar td").all()

# selecting date from the date picker.
    for dt in all_dates:
        date_text=dt.inner_text()
        if(date_text==target_date):
            dt.click()
            break



def test_jquery_date_picker(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    date_input = page.locator("#datepicker")
    
    # #apporach 1
    # date_picker.fill("07/23/2004")  #(mm/dd/yyyy)
    
    #approach 2
    is_future = True
    year = "2027"
    month = "June"
    date = "2"

    date_input.click() #opens datepicker
    select_date(page,year,month,date,is_future)
    print("Selected Date ====>:",date_input.input_value())
    expect(date_input).to_have_value("06/02/2027")


    page.wait_for_timeout(5000)
