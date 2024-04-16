from behave import *
from main import get_zodiac_sign


@given('the user has entered their birthday as "{birthday}"')
def step_impl(context, birthday):
    context.birthday = birthday

@when('the user requests their zodiac sign')
def step_impl(context):
    context.zodiac_sign = get_zodiac_sign(context.birthday)

@then('the zodiac sign "{expected_sign}" should be returned')
def step_impl(context, expected_sign):
    assert context.zodiac_sign == expected_sign
