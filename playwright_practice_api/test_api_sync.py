import json
import time

import pytest
from playwright.sync_api import Playwright, APIRequestContext, Page, expect
from typing import Generator, Any

from playwright_practice.conftest import user_credentials
from playwright_practice_api.conftest import api_new_context





payload = {
  "orders": [
    {
      "country": "United States",
      "productOrderedId": "67a8dde5c0d3e6622a297cc8"
    }
  ]
}

@pytest.mark.smoke
def test_create_order(get_token, api_new_context):
    response = api_new_context.post(url="/api/ecom/order/create-order", data=payload, headers= {"Authorization": get_token, "Content-Type": "application/json"})
    assert response.ok
    response_body = response.json()
    print(response_body)


def intercept_response(route):
    route.fulfill(
        json = {
            "data":[],"message":"No Orders"
        }
    )
def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=/681a7126fd2af1c99e127af4")

@pytest.mark.interception
def test_interception(page: Page):
    page.goto("/client")
    page.locator("#userEmail").fill("jabbarova.leyla@gmail.com")
    page.locator("#userPassword").fill("T0gether@")
    page.locator("#login").click()
    page.route(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",handler=intercept_response)
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("You have No Orders to show at this time.")).to_be_visible()

@pytest.mark.interception
def test_interception_request(page: Page):
    page.goto("/client")
    page.locator("#userEmail").fill("jabbarova.leyla@gmail.com")
    page.locator("#userPassword").fill("T0gether@")
    page.locator("#login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.route(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",handler=intercept_request)
    page.get_by_role("button", name="View").first.click()
    expect(page.locator(".blink_me")).to_contain_text("You are not authorize to view this order")




