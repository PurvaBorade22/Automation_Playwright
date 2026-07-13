import pytest
from playwright.sync_api import Page,expect

def test_frames(page:Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    #frame 3
    frame3= page.frame(url ="https://ui.vision/demo/webtest/frames/frame_3")

    frame3.locator("input[name='mytext3']").fill("Welcome")
    page.wait_for_timeout(3000)

    child_frame = frame3.child_frames
    print("number of Child frame are:-",len(child_frame))

    inner_frame=child_frame[0]

    radio = inner_frame.get_by_label("I am a human")
    radio.check()

    expect(radio).to_be_checked()

    page.wait_for_timeout(5000)
