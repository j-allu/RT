*** Settings ***
Library     ../Python/functions.py
Library     ../Python/control.py
Library     ../Python/classes.py

*** Test Cases ***
First example
    Simple
    ${greeting} =    Simple
    Should be equal    ${greeting}    Hello, world!

Arguments
    ${result} =    One argument    Robot
    Should be equal    ${result}    Hello, Robot!
    ${result} =    Two arguments    1    2
    Should be equal as integers    ${result}    3
    Should be equal    ${result}    ${3}

Default values
    ${result} =    Defaults    Robot
    Should be equal    ${result}    Hello, Robot!
    ${result} =    Defaults    Robot    !!!!
    Should be equal    ${result}    Hello, Robot!!!!

Named argument syntax
    ${result} =    Defaults    Kitty    separator=${SPACE}
    Should be equal    ${result}    Hello Kitty!
    ${result} =    Defaults    for the last time    separator=${SPACE}    ending=...
    Should be equal    ${result}    Hello for the last time...

Failures
    Should be positive    42
    Should be positive    -2

Errors
    Should be positive    not a number

Objects as return values and arguments
    ${jane} =    Create Person    Jane
    ${john} =    Create Person    John    john@example.com
    Greet Person    ${jane}    ${john}

Extended variable syntax
    ${jane} =    Create Person    Jane
    ${john} =    Create Person    John    john@example.com
    # Accessing attributes is clear and easy to understand.
    Should be equal    ${jane.name}    Jane
    Should be equal    ${jane.email}    ${NONE}
    Should be equal    ${john.email}    john@example.com
    # Calling methods, especially when they require arguments, is questionable.
    # Use a dedicated keyword, like above 'Greet Person', instead.
    Log    ${jane.greet('${john.name}')}
