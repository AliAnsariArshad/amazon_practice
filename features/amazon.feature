Feature: Amazon test
  Background:
    Given User open the Amazon web portal

  @laptop
  Scenario: Adding a “Monitor” Item in Cart and verifying sub total
    When User enter the "Monitor" in search box and hit enters
    And User selects the "first" item from the list
    And User click on add to cart button
    And User clicks on cart button
    Then User Verifies that the price is identical to the product page
    And user verifies subtotal is similar to the price

  @laptop
  Scenario: Adding a “Laptop” Item in Cart and verifying sub total
    When User enter the "Laptop" in search box and hit enters
    And User selects the "second" item from the list
    And User click on add to cart button
    And User clicks on cart button
    Then User Verifies that the price is identical to the product page
    And user verifies subtotal is similar to the price

  @scenario3
  Scenario: Verify subtotal Item in Cart and verifying sub total
    When User enter the "Headphone" in search box and hit enters
    And User selects the "first" item from the list
    And User click on add to cart button
#    When User enter the "Keyboard" in search box and hit enters
#    And User selects the "first" item from the list
#    And User click on add to cart button
#    And User clicks on cart button
#    Then User Verifies that the price is identical to the product page
#    Then user verifies subtotal is similar to the price
