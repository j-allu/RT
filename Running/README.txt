Here we have scripts with different approaches to run tests.

run_tests.bat:
    Windows batch file to run tests with certain default options. Accepts path
    to tests to be executed as additional command line options and passes them
    directly to Robot Framework.

run_tests.sh:
    Shell script with same functionality as the above batch file.

run_tests.py:
    Python file with same functionality as the above scripts. Handy when need
    to run same runner script in different operating systems or if the script
    needs to have more logic.

run_tests2.py:
    Using a bit lower level API to run tests using Python.

run_tests3.py:
    Using even lower level APIs. This approach makes it possible to freely
    modify tests and results but is also more complicated than the earlier
    solutions. Using model modifiers introduced in the `Modifiers` directory
    is often a simpler solution to modify tests or results.


Robot Framework's API used by the Python scripts is documented at
http://robot-framework.readthedocs.org/.
