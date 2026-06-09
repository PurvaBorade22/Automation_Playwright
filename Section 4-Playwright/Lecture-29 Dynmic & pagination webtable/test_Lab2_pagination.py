import pytest
from playwright.sync_api import Page,expect

def test_lab2_pagination_table(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #get all pagination link
    pages = page.locator("ul#pagination li").all()
    page_count = len(pages)
    print("Number of Pages:",page_count)

    for page_index in range(page_count):
        pages[page_index].click()

        rows = page.locator("#productTable tbody tr").all()
        for row in rows:
            id = row.locator("td").nth(0).inner_text()
            name = row.locator("td").nth(1).inner_text()
            price = row.locator("td").nth(2).inner_text()

            row.locator("td").nth(3).locator("input").check()

            print(id, "\t",name,"\t",price)

        page.wait_for_timeout(3000)