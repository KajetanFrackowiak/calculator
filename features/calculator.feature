Feature: Calculator operations
  In order to avoid silly mistakes
  As a user
  I want to use a calculator to add, subtract and multiply numbers

  Scenario: Add two numbers
    Given the numbers 3 and 5
    When I add the numbers
    Then the result should be 8

  Scenario: Subtract two numbers
    Given the numbers 10 and 4
    When I subtract the numbers
    Then the result should be 6

  Scenario: Multiply two numbers
    Given the numbers 7 and 6
    When I multiply the numbers
    Then the result should be 42
