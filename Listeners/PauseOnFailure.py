"""Listener that stops execution if a test fails."""

ROBOT_LISTENER_API_VERSION = 2


def end_test(name, info):
    if info['status'] == 'FAIL':
        raw_input('\nTest "{}" failed with error "{}".'
                  '\nPress <enter> to continue.'.format(name, info['message']))
