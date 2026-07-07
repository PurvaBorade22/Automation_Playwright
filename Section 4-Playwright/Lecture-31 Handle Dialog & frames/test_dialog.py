import pytest
from playwright.sync_api import Page,expect

@pytest.mark.skip
def test_dialog_1(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # Apporach 1
    # Registering an event
    def handle_dialog(dialog):
        dialog.accept()

    page.on("dialog",handle_dialog)
    page.wait_for_timeout(5000)

    page.locator("#alertBtn").click()

    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_dialog_2(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.on("dialog",lambda dialog:dialog.accept())
    page.wait_for_timeout(5000)

    page.locator("#alertBtn").click()
    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_confirmation_alert(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.on("dialog",lambda dialog:dialog.dismiss())
    page.wait_for_timeout(3000)

    page.locator("#confirmBtn").click()
    page.wait_for_timeout(3000)

    text= page.locator("#demo").inner_text()
    print("The output is-->",text)

    expect(page.locator("#demo")).to_have_text("You pressed Cancel!")
    page.wait_for_timeout(5000)

def test_prompt_alert(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.on("dialog",lambda dialog:dialog.accept('John'))
    page.wait_for_timeout(3000)

    page.locator("#promptBtn").click()
    page.wait_for_timeout(3000)

    text= page.locator("#demo").inner_text()
    print("The output is:-->",text)

    expect(page.locator("#demo")).to_have_text("Hello John! How are you today?")
    page.wait_for_timeout(5000)