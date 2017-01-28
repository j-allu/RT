class LibraryWithListener(object):
    ROBOT_LISTENER_API_VERSION = 2
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self
        self.keyword_calls = {}

    # Listener method. Can start with an underscore in this context to
    # avoid creating keyword.
    def _start_keyword(self, name, attrs):
        if name not in self.keyword_calls:
            self.keyword_calls[name] = 0
        self.keyword_calls[name] += 1

    # Normal keyword
    def log_keyword_calls(self):
        for name, count in sorted(self.keyword_calls.items()):
            print('Keyword "{}" was called {} times.'.format(name, count))
