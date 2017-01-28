from __future__ import print_function


class HybridLibrary(object):

    def __init__(self):
        self.keywords = ['hybrid_keyword', 'external_hybrid_keyword']
        self.external = ExternalComponent()

    def get_keyword_names(self):
        """Return names of the keywords implemented by this library."""
        return self.keywords

    def hybrid_keyword(self):
        """Hybrid keyword implemented directly in the library itself.

        Arguments and docstrings are got using introspection from the method
        just like with the normal static library API. No need for special
        `get_keyword_arguments/documentation` methods like with the dynamic API.
        """
        print('Hello, hybrid world!')

    def not_keyword(self):
        """Not returned by get_keyword_names and thus not usable as keyword."""
        pass

    def __getattr__(self, name):
        """Dispatcher for possible externally/dynamically implemented keywords.

        Notice that need to *return* a function that is used as a keyword here,
        not run a keyword directly like in the dynamic API's `run_keyword`
        method.

        Arguments and docstrings are got using introspection from the returned
        function.
        """
        if name in self.keywords:
            return getattr(self.external, name)
        raise AttributeError(name)


class ExternalComponent(object):

    def external_hybrid_keyword(self):
        """Hybrid keyword implemented in an external component."""
        print('Hello, external hybrid world!')
