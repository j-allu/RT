"""Pre-run modifier to select only every Xth test case for execution.

Usage:
    robot --prerunmodifier RunEveryXth.py[:x][:start] path/to/tests.robot
"""

from robot.api import SuiteVisitor


class RunEveryXth(SuiteVisitor):

    def __init__(self, x=2, start=0):
        self.x = int(x)
        self.start = int(start)

    def start_suite(self, suite):
        suite.tests = suite.tests[self.start::self.x]

    def visit_test(self, test):
        pass
