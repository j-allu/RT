*** Settings ***
Library          LibraryWithListener.py
Test Teardown    Log keyword calls

*** Test Cases ***
Passing
    No operation
    Log    I don't do much...

Failing
    Log    This is about to fail!!!
    Fail    Expected error
