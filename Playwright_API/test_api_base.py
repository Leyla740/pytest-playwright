from http.client import responses
import json
import pytest

from playwright.sync_api import Playwright

from Playwright_API.conftest import user_credentials

payload = {
  "orders": [
    {
      "country": "United States",
      "productOrderedId": "67a8dde5c0d3e6622a297cc8"
    }
  ]
}

# payload1 = {
#       "userEmail": "devop740@gmail.com",
#       "userPassword": "T0gether@"
#     }

class APIUtils:

#get token post request/login
    def get_token(self, playwright: Playwright, user_credentials: dict):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login", data={"userEmail": user_credentials["userEmail"], "userPassword": user_credentials["userPassword"]})

        assert response.ok
        response_body = response.json()
        print(response_body)
        return response_body["token"]

#create an order post request
    def create_order_api(self, playwright: Playwright, user_credentials: dict):
        token = self.get_token(playwright, user_credentials)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data = payload,
                                 headers = {"Authorization": token,
                                            "Content-Type": "application/json"}
                                            )
        print(response.json())
        response_body1 = response.json()
        order_id = response_body1["orders"][0]
        return order_id

