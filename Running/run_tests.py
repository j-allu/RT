#!/usr/bin/env python

import sys
from robot import run_cli

print('Some pre-task...')
# `exit=False` only supported by RF 3.0.1 and newer. With earlier you need
# to use `try/except SystemExit` to avoid exiting as part of `run_cli` call.
run_cli(['--name', 'Example', '--dotted'] + sys.argv[1:], exit=False)
print('Some post-task...')
