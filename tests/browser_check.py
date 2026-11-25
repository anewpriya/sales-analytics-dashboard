from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1280, "height": 900})
    errors = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.goto("http://127.0.0.1:5000/")
    page.get_by_text("36.85%", exact=True).first.wait_for()
    page.locator("select").select_option("Daily")
    page.get_by_role("table").first.wait_for()
    assert page.locator(".number").count() == 4
    page.locator("select").select_option("all")
    page.get_by_text("36.85%", exact=True).first.wait_for()
    page.set_viewport_size({"width": 390, "height": 844})
    assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth")
    assert not errors, errors
    browser.close()
print("Browser smoke test passed")
