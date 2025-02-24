import playwright
from playwright.sync_api import sync_playwright

DEFAULT_TIMEOUT=10000

def before_feature(context, feature):
    context.feature_data = {}
    if "gui" in feature.tags:
        context.playwright = sync_playwright().start()
        context.browser = context.playwright.chromium.launch(headless=True)

def before_scenario(context, scenario):
    # This hook runs before each scenario.
    if "gui" in scenario.effective_tags:
        context.page = context.browser.new_page()
        # Set default timeout for waiting on elements and navigation
        context.page.set_default_timeout(DEFAULT_TIMEOUT)
        context.page.set_default_navigation_timeout(DEFAULT_TIMEOUT)

def after_scenario(context, scenario):
    # This hook runs after each scenario.
    if "gui" in scenario.effective_tags:
        context.page.close()

def after_feature(context, feature):
    if "gui" in feature.tags:
        context.browser.close()
        context.playwright.stop()