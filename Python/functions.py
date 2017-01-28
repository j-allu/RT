from __future__ import print_function


def simple():
    print('*DEBUG* Hi there!')
    return 'Hello, world!'


def one_argument(name):
    # Old string formatting style
    return 'Hello, %s!' % name
    # Newer string formatting
    return 'Hello, {}!'.format(name)


def two_arguments(number1, number2):
    return int(number1) + int(number2)


def defaults(name, ending='!', separator=', '):
    # Old string formatting. Parentheses needed with more than one value.
    return 'Hello%s%s%s' % (separator, name, ending)
    # Newer formatting
    return 'Hello{}{}{}'.format(separator, name, ending)
    # Newer formatting with custom indices
    return 'Hello{2}{0}{1}'.format(name, ending, separator)
    # Newer formatting with named placeholders
    return 'Hello{sep}{name}{end}'.format(name=name, end=ending, sep=separator)


def varargs(*numbers):
    result = 0
    for num in numbers:
        result += num    # equivalent to `result = result + num`
    return result


# Alternatively, and better, using built-in function `sum`.
def varargs(*numbers):
    return sum(numbers)


def kwargs(**kws):
    result = []
    for key in sorted(kws):
        result.append('{}: {}'.format(key, kws[key]))
    return ', '.join(result)


# Alternatively iterating items, not keys.
def kwargs(**kws):
    result = []
    for key, value in sorted(kws.items()):
        result.append('{}: {}'.format(key, value))
    return ', '.join(result)


# Alternatively using a generator expression (similar to list comprehension).
def kwargs(**kws):
    return ', '.join('{}: {}'.format(key, kws[key]) for key in sorted(kws))


def caller(func, *args, **kwargs):
    return func(*args, **kwargs)
