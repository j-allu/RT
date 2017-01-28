#!/usr/bin/env python

"""Utility to mark test that take too long time failed.

Can be used either as a separate script or as a pre-Rebot modifier as part of
test execution or when using Rebot.

Usage as a script:
    {tool} path/to/output.xml max_seconds

Usage as a modifier:
    robot --prerebotmodifier {tool}:max_seconds path/to/tests.robot
    rebot --prerebotmodifier {tool}:max_seconds path/to/output.xml
"""

import sys
from robot.api import SuiteVisitor, ExecutionResult


class FailSlowTests(SuiteVisitor):

    def __init__(self, max_seconds):
        self.max_seconds = float(max_seconds)

    def visit_test(self, test):
        if test.passed and test.elapsedtime > self.max_seconds * 1000:
            test.status = 'FAIL'
            test.message = 'Test was slower than %0.3f s.' % self.max_seconds


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__.format(tool=sys.argv[0]))
    path, max_time = sys.argv[1:]
    result = ExecutionResult(path)
    result.suite.visit(FailSlowTests(max_time))
    result.save()
    sys.exit(result.return_code)
