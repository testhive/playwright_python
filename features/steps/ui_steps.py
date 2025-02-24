from behave import given, when, then,step
from playwright.sync_api import sync_playwright

@step('I navigate to "{url}"')
def step_navigate(context, url):
    # Start Playwright and launch a browser
    context.page.goto(url)

@step('I search for "{query}"')
def step_search(context, query):
    context.page.fill('input[name="search"]', query)
    context.page.click('.cdx-search-input__end-button   ')

@step('The result page should contain "{text}"')
def step_verify(context, text):
    # Get the page content and assert that the expected text is present
    content = context.page.content()
    assert text.lower() in content.lower(), f"Expected to find '{text}' in page content."

