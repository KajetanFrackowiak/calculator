from behave import given, when, then
from main import add, subtraction, multiply

@given('the numbers {num1:d} and {num2:d}')
def step_given_numbers(context, num1, num2):
    context.num1 = num1
    context.num2 = num2

@when('I add the numbers')
def step_when_add(context):
    context.result = add(context.num1, context.num2)

@when('I subtract the numbers')
def step_when_subtract(context):
    context.result = subtraction(context.num1, context.num2)

@when('I multiply the numbers')
def step_when_multiply(context):
    context.result = multiply(context.num1, context.num2)

@then('the result should be {expected:d}')
def step_then_result_should_be(context, expected):
    assert context.result == expected
