# Lab 6 Review Questions

## 1. Why should you mock a payment gateway in tests? Give two distinct reasons.

I mock a payment gateway to avoid making actual financial transactions that charge real money during test execution, and to ensure my tests run fast and reliably without depending on an external network connection.

## 2. What is the difference between return_value and side_effect?

I use `return_value` to return a fixed response every time the mock is called, whereas I use `side_effect` to dynamically return different values across sequential calls, raise exceptions, or execute a custom callable function.

## 3. Module app does 'import requests' and calls requests.get. What do you patch?

I patch `app.requests.get` (or `app.requests`) because I must patch the object where it is used and looked up, rather than where it is originally defined in the `requests` library.

## 4. Why can a mistyped assertion method make a test pass, and how do you prevent it?

A mistyped assertion method on a `MagicMock` (such as `assert_called_withh`) causes Python to dynamically create a new mock attribute instead of raising an error, silently letting the test pass without validating anything. I prevent this by passing `autospec=True` to `@patch` or setting `unsafe=False` on the mock so that calling invalid methods raises an `AttributeError`.

## 5. Name one thing you should NOT mock, and say why.

I should not mock my own core business logic or domain code because doing so hides potential bugs in the actual system behavior and turns the test into a meaningless verification of the mock itself.