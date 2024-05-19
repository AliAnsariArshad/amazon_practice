Feature: Amazon test
  Scenario: Adding a “Monitor” Item in Cart and verifying sub total
    Given User open the Amazon web portal
    When User enter the "Monitor" in search box and hit enters
    And User selects the first item from the list
    And User click on add to cart button
    And User clicks on cart button
    Then User Verifies that the price is identical to the product page
    Then user verifies subtotal is similar to the price
