#!/usr/bin/env python

"""Script to parse, modify and and run tests programmatically.

Usage: %s path/to/tests.robot
"""

import sys
from robot.api import TestSuiteBuilder, ResultWriter


if len(sys.argv) != 2:
    sys.exit(__doc__ % sys.argv[0])

path = sys.argv[1]
suite = TestSuiteBuilder().build(path)
suite.name = 'Example'
test = suite.tests.create(name='Created', tags=['example'])
test.keywords.create(name='Log', args=['Hello, world!'])
result = suite.run(dotted=True, output='output.xml')

writer = ResultWriter('output.xml')
writer.write_results(log='log.html', report='report.html')

sys.exit(result.return_code)
