*** Settings ***
Library        CalculatorLibrary.py

*** Test Cases ***
Pushing buttons
    Push button    1
    Push button    2
    Result should be    12

Simple calculation
    Push button    1
    Push button    +
    Push button    2
    Push button    =
    Result should be    3

Clear
    Push button    7
    Push button    C
    Result should be    ${EMPTY}

Longer calculation
    Push buttons    1 + 2 - 3 * 4 =
    Result should be    -9

Longer calculation (with template)
    [Template]    Calculation result should be
    1 + 2 - 3 * 4    -9
    10 * 10 - 99     1
    -2 * 10 + 42     22

Invalid calculations
    [Template]    Calculation should fail
    invalid      Invalid button 'i'.
    1 + / 2      Invalid expression '1+/2'.
    1 / 0        Division by zero.

BDD style test
    Given calculator is cleared
    When calculation "1 + 2 - 3 * 4" is evaluated
    Then result should be "-9"


# BDD style keywords could also be implemented as Robot's user keywords.
#
#*** Keywords ***
#Calculator is cleared
#    [Tags]    bdd
#    Push button    C
#
#Calculation "${expression}" is evaluated
#    [Tags]    bdd
#    Push buttons    ${expression}=
#
#Result should be "${expected}"
#    [Tags]    bdd
#    Result should be    ${expected}
