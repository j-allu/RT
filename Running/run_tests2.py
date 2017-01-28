#!/usr/bin/env python

"""Script to run tests using `robot.run` API.

Usage: %s path/to/tests.robot
"""

import sys
from robot import run

if len(sys.argv) != 2:
    sys.exit(__doc__ % sys.argv[0])

path = sys.argv[1]
rc = run(path, name='Example', dotted=True)
sys.exit(rc)
