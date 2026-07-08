import pytest
from playwright.sync_api import Page,expect

def test_frames(page:Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    frames = page.frames
    print("Number os frames:-",len(frames))

    # frame 1
    frame1 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_1")
    inputtext= frame1.locator("input[name='mytext1']")
    inputtext.fill("welcome")

    page.wait_for_timeout(5000)
