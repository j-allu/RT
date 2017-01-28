This directory contains training material related to creating test libraries
for Robot Framework.

- `basics.robot` uses earlier created Python modules as test libraries.

- `calculator.robot` is a bit more realistic example with a class based
  test library `CalculatorLibrary.py` that is used for testing a simple
  calculator in `calculator.py`. This library also demonstrates using
  `@keyword` decorator and embedded arguments.

- `DynamicLibrary.py` and `HybridLibrary.py` contain examples of the dynamic
  and hybrid library APIs, respectively. These libraries are used by simple
  tests in `dynamic_and_hybrid.robot`.

Robot Framework User Guide has a dedicated section explaining how to create
test libraries:
http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-test-libraries

There is a also a demo project that has the same calculator and very similar
test library as our `CalculatorLibrary.py`:
https://bitbucket.org/robotframework/robotdemo/

The created `CalculatorLibrary.py` contains library and keyword documentation
as class and method docstrings. Libdoc tool was used to create HTML documentation
based on them and results are in `CalculatorLibrary.html`. For more details about
Libdoc see the User Guide:
http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#libdoc
