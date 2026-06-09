import pytest

from playwright.sync_api import Page,expect

@pytest.mark.skip
def test_pagination_table(page:Page):
    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")

    has_more_pages = True

    while has_more_pages:
        rows=page.locator("#example tbody tr").all()
        for row in rows:
            print(row.inner_text())
            page.wait_for_timeout(2000)

        next_button= page.locator("button[aria-label='Next']")
        is_disabled = next_button.get_attribute("class")

        if "disabled" in is_disabled:
            has_more_pages = False
        else:
            next_button.click()

def test_filter_row(page:Page):
    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")

    dropdown = page.locator("#dt-length-0")
    dropdown.select_option(label="25")

    rows=page.locator("#example tbody tr")
    print("No. of rows:",rows.count())
    expect(rows).to_have_count(25)

