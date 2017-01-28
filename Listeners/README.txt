This directory demonstrates Robot Frameworks listener interface.

`PauseOnFailure.py` is a listener that can be used from the command line to
stop execution if a test fails:

    robot --listener PauseOnFailure.py tests.robot

`LibraryWithListener.py` is a test library that register itself as a listener.
It is used by `tests.robot`.

Both the normal listener interface and the library listener interface are
documented in the Robot Framework User Guide:
http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#using-listener-interface
