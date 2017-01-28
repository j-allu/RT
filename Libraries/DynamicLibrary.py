from __future__ import print_function


class DynamicLibrary(object):

    def get_keyword_names(self):
        """Return names of the keywords implemented by this library."""
        return ['Dynamic keyword', 'Keyword with arguments']

    def run_keyword(self, name, args):
        """Run the specified keyword with the specified arguments.

        In the simplest case logic can be directly here, but in most cases
        logic is somewhere else and this method just handles dispatching.

        Reporting status, logging, returning values, etc. is handled just
        like in the static library API.
        """
        print('Running keyword "{}" with arguments {}.'.format(name, args))

    def get_keyword_arguments(self, name):
        """Optional method to return keyword argument specification.

        Information is used during execution to check are arguments used
        correctly and by Libdoc when generating library documentation.
        """
        if name == 'Keyword with arguments':
            return ['first', 'second=default value']
        return []

    def get_keyword_documentation(self, name):
        """Optional method to return keyword/library documentation.

        Mainly used by Libdoc. Special value `__intro__` used to get
        documentation for the library itself.
        """
        if name == '__intro__':
            return 'Documentation for our cool dynamic library.'
        return 'Documentation for keyword "{}".'.format(name)
