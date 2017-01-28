*** Settings ***
Variables        simple.py
Variables        dynamic.py    arg

*** Test Cases ***
Simple
    Should be equal    ${STRING}    Hello, world!
    Should be equal    ${INTEGER}    ${42}
    Length should be    ${LIST}    3

Dynamic
    Should be equal    ${DYNAMIC}    Hello, arg!
    Should be empty    ${ANOTHER DYNAMIC}
