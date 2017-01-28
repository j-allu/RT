This directory contains Python training material.

Files starting with `test_` contain exercises. They can be executed with
`py.test` tool that can be installed with `pip install pytest` and used like:

    py.test test_functions.py       # run all tests in test_functions.py
    py.test test_functions.py -x    # same but stop on the first failure
    py.test .                       # run all tests in the current directory

Additional Python files need to be created to make tests pass. See test files
themselves for more details. The recommended order to go through the exercises
is:

    test_functions.py
    test_control.py
    test_classes.py
