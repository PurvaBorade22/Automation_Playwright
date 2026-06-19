import pytest
from playwright.sync_api import Page,expect

def select_booking_date(page,booking_year,booking_month,booking_date):
    while True:
        current_year = page.locator("span.ui-datepicker-year").inner_text()
        current_month = page.locator(".ui-datepicker-month").inner_text()

        if current_month == booking_month and current_year == booking_year:
            break
        else:
            page.locator(".ui-datepicker-next-icon").click()

    #select date
    all_dates = page.locator("table.ui-datepicker-calendar tbody td a").all()

    for date in all_dates:
        if date.inner_text() == booking_date:
            date.click()
            break

def test_lab4_IRCTC(page:Page):
    page.goto("https://www.irctc.co.in/nget/train-search")

    page.locator("div[aria-label='Header'] button:nth-child(2)").click()

    date_input= page.locator("#jDate span input")
    date_input.click()

    booking_year = "2026"
    booking_month = "June"
    booking_date = "30"

    select_booking_date(page,booking_year,booking_month,booking_date)
    
    select_date = date_input.input_value()
    print("selected date ===>:",select_date)
    expect(date_input).to_have_value("30/06/2026")

    page.wait_for_timeout(5000)