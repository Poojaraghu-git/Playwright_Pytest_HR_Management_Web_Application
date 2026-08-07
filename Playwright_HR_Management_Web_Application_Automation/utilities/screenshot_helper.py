class ScreenshotHelper:
    def __init__(self, page):
        self.page = page

    def take_screenshot(self, name):
        self.page.screenshot(path=f"screenshots/{name}.png", full_page=True)
