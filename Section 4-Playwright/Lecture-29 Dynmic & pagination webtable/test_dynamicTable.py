import pytest

from playwright.sync_api import Page,expect

def test_dynamic_table(page:Page):

    page.goto("https://practice.expandtesting.com/dynamic-table")

    table = page.locator("table.table tbody")

    #get all the rows
    rows = table.locator("tr").all()

    #comparing
    cpu_load = ""
    for row in rows:
        process_name =row.locator("td").nth(0).inner_text()
        if process_name=="Chrome":
            cpu_load = row.locator("td:has-text('%')").inner_text()
            print("Cpu load is:",cpu_load)
            break
    
    expect(page.locator("#chrome-cpu")).to_contain_text(cpu_load)

    page.wait_for_timeout(5000)

