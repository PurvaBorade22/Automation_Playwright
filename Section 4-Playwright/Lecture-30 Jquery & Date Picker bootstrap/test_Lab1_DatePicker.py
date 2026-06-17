import pytest

from playwright.sync_api import Page,expect

def select_date(page,target_year,target_month,target_date):
    #select year
    year_dropdown = page.locator("select.ui-datepicker-year")
    year_dropdown.select_option(label=target_year)

    #select month
    month_dropdown = page.locator("select[aria-label='Select month']")
    month_dropdown.select_option(label=target_month)

    #clicked on date
    all_dates = page.locator("table.ui-datepicker-calendar a")
    for i in range(all_dates.count()):
        date_element = all_dates.nth(i)
        if date_element.inner_text() == target_date:
            date_element.click()
            break

def test_Lab1_DatePicker(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    date_picker = page.locator("#txtDate")
    date_picker.click()

    select_date(page,'2026','Jun','30')

    expect(date_picker).to_have_value('30/06/2026')

    page.wait_for_timeout(5000)