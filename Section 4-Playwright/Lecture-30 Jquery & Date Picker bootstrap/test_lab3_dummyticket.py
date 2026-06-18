import pytest

from playwright.sync_api import Page,expect

def select_date_of_birth(page,birth_year,birth_month,birth_date):
    # for year
    page.locator("select[aria-label='Select year']").select_option(birth_year)

    #month
    page.locator("select[aria-label='Select month']").select_option(birth_month)

    #for dates
    date_cells = page.locator("table.ui-datepicker-calendar td a").all()
    for cell in date_cells:
        if cell.text_content() == birth_date:
            cell.click()
            break

def select_date(page,dep_year,dep_month,dep_date):
    #dep year
    page.locator("select[aria-label='Select year']").select_option(dep_year)

    #dep month
    page.locator("select[aria-label='Select month']").select_option(dep_month)

    #for dates
    dep_dates = page.locator("table.ui-datepicker-calendar td a").all()
    for date in dep_dates:
        if date.text_content() == dep_date:
            date.click()
            break


def test_dummy_ticket_booking(page:Page):
    page.goto("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

    #2 Select Ticket Type: 
    page.locator("#product_549").check()
    expect(page.locator("#product_549")).to_be_checked()

    #3 Enter Passenger Details: 
    page.locator("#travname").fill("Akash")
    page.locator("#travlastname").fill("Ratore")
    
    #select DOB
    birth_year = "2004"
    birth_month = "Jul"
    bith_date = "22"
    page.locator("#dob").click()
    select_date_of_birth(page,birth_year,birth_month,bith_date)

    page.locator("#sex_1").click()
    expect(page.locator("#sex_1")).to_be_checked()

    # 4 Enter Travel Details:
    page.locator("#traveltype_1").click()
    expect(page.locator("#traveltype_1")).to_be_checked()

    page.locator("#fromcity").fill("Toronto")
    page.locator("#tocity").fill("Mumbai")

    dep_year = "2026"
    dep_month= "Nov"
    dep_date = "10"
    page.locator("#departon").click()
    select_date(page,dep_year,dep_month,dep_date)

    #5. Additional Information:
    page.locator("#notes").fill( "Need visa as soon as possible.")

    #6. Delivery Options:
    page.locator("#select2-reasondummy-container").click()

    app_year = "2026"
    app_month = "Oct"
    app_date = "20"
    page.locator("#appoinmentdate").click()
    select_date(page,app_year,app_month,app_date)

    #to check if it select
    app_value= page.locator("#appoinmentdate").input_value()
    print("Appointment date ==>",app_value)
    expect(page.locator("#appoinmentdate")).to_have_value("20/10/2026")

    page.locator("#deliverymethod_1").click()

    #7. Enter Billing Details: 
    page.locator("#billname").fill("Akash Rathore")
    page.locator("#billing_phone").fill("+12345678956")
    page.locator("#billing_email").fill("abc.123@gmail.com")
    # page.locator("#billing_city").fill("AIroli")

    #country
    page.locator('#select2-billing_country-container').click()
    page.locator('.select2-results li:has-text("Canada")').click()

    #town
    page.locator("#billing_city").fill("abc")

    #Province
    page.locator('#select2-billing_state-container').click()
    page.locator('.select2-results li:has-text("Ontario")').click()

    #pincode
    page.locator("#billing_postcode").fill("123455")

    

    page.locator("#billing_address_1").fill("123 Scott Street, Niagara Falls, Ontario, L2C 6M1")

    # 8. verify table name
    product_name = page.locator(".product-details")
    print("Product name ===>",product_name.inner_text())
    expect(product_name).to_have_text("Dummy ticket for Visa Application")

    product_price = page.locator(".shop_table.woocommerce-checkout-review-order-table tfoot tr:nth-child(2) td")
    print("Product price ====>",product_price.inner_text())
    expect(product_price).to_have_text("₹1,200")

    page.locator("#place_order").click()


    page.wait_for_timeout(9000)

   
