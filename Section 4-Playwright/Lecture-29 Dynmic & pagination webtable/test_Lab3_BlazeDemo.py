import pytest
from playwright.sync_api import Page, expect

def test_travel_agency(page:Page):
    page.goto("https://blazedemo.com/")

    # step 2 select depature and destination
    page.locator("select[name='fromPort']").select_option(label="Boston")
    page.locator("select[name='toPort']").select_option(label="New York")

    #step 3: click on button
    page.locator("input[type='submit']").click()

    #step4:Capture Flight Prices 
    rows = page.locator(".table tbody tr")
    row_count = rows.count()

    #6.
    prices = []
    for i in range(row_count):
        price_text = rows.nth(i).locator("td").nth(5).inner_text()
        prices.append(price_text)
    
    flight_count = rows.count()
    print("Total no. of flights are available:",flight_count)

    # step 7:
    sorted_prices = sorted(prices)
    lowest_price = sorted_prices[0]
    print("Lowest Price:",lowest_price)

    # find lowest price and lick the button
    for i in range(row_count):
        price_text =rows.nth(i).locator("td").nth(5).inner_text()
        if price_text == lowest_price:
            rows.nth(i).locator("td input[type='submit']").click()
            break
    
    #9.filling passenger details 
    page.locator("#inputName").fill("John")
    page.locator("#address").fill("1403 American Beauty Ln")
    page.locator("#city").fill("Columbus")
    page.locator("#state").fill("OH")
    page.locator("#zipCode").fill("43240")
    page.locator("#cardType").select_option("American Express")
    page.locator("#creditCardNumber").fill("6789 0673 4523 1267")
    page.locator("#creditCardMonth").fill("2023")
    page.locator("#creditCardYear").fill("2026")
    page.locator("#nameOnCard").fill("John Canedy")

    # 9.click on purchase flight button
    page.locator("input[type='submit']").click()

    #validate msg
    expect(page.locator("h1")).to_have_text("Thank you for your purchase today!")
    
    page.wait_for_timeout(4000)