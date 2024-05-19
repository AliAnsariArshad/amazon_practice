import time

from behave import *
from features.page_repository.home_page import HomePage


@given(u'User open the Amazon web portal')
def step_impl(context):
    context.home_page = HomePage(context.driver)


@when(u'User enter the "{text}" in search box and hit enters')
def step_impl(context, text):
    context.home_page.enter_in_search_box(text)


@when(u'User selects the first item from the list')
def step_impl(context):
    context.home_page.select_item()


@when(u'User click on add to cart button')
def step_impl(context):
    context.price = context.home_page.return_product_price()
    context.price_1 = context.price.strip() + ".00"
    context.home_page.add_to_cart()


@when(u'User clicks on cart button')
def step_impl(context):
    context.home_page.click_on_cart_button()


@then(u'User Verifies that the price is identical to the product page')
def step_impl(context):
    context.total_price = context.home_page.return_cart_product_price().strip()
    assert context.price_1 == context.total_price, (f"price is not same, expected price is {context.price_1} | "
                                                  f"actaul price is {context.total_price}")


@then(u'user verifies subtotal is similar to the price')
def step_impl(context):
    context.subtotal = context.home_page.return_subtotal().strip()
    assert context.price_1 == context.subtotal, (f"price is not same, expected price is {context.price_1} | "
                                               f"actaul price is {context.subtotal}")

