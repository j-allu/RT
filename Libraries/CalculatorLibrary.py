from robot.api import logger
from robot.api.deco import keyword

# If having `robot.api` as a dependency is a problem, it is possible to use
# the standard `logging` module instead.
#import logging

from calculator import Calculator, CalculationError


class CalculatorLibrary(object):
    """Library for testing *Calculator*.

    Uses ``push()`` method for interaction.
    """

    # Controls when Robot creates new instance of the library. Possible values
    # are 'GLOBAL', 'TEST SUITE' and 'TEST CASES' (default).
    #ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self.calculator = Calculator()
        self.result = ''

    def push_button(self, button):
        """Pushes the specified ``button``.

        Use `Push Buttons` if you need to push several buttons.
        """
        logger.info('Pushing button <b>{}</b>.'.format(button), html=True)
        #logging.info('Pushing button "{}".'.format(button))
        self.result = self.calculator.push(button)

    def push_buttons(self, expression):
        """Pushes all the buttons in the ``expression`` one by one."""
        for button in expression.replace(' ', ''):
            self.push_button(button)

    def result_should_be(self, expected):
        if self.result != expected:
            raise AssertionError('Expected result to be "{}" but it was "{}".'
                                 .format(expected, self.result))

    def calculation_result_should_be(self, expression, expected):
        self.push_buttons('C' + expression + '=')
        self.result_should_be(expected)

    def calculation_should_fail(self, expression, expect_error):
        try:
            self.push_buttons('C' + expression + '=')
        except CalculationError as err:
            if str(err) != expect_error:
                raise AssertionError('Expected error "{}" but got "{}".'
                                     .format(expect_error, err))
        else:
            raise AssertionError('Expected error "{}" did not occur.'
                                 .format(expect_error))

    # BDD style keywords. Could/should be moved into own library.

    @keyword(tags=['bdd'])
    def calculator_is_cleared(self):
        self.push_button('C')

    @keyword('Calculation "${expression}" is evaluated', tags=['bdd'])
    def calculation_is_evaluated(self, expression):
        self.push_buttons(expression + '=')

    @keyword('Result should be "${expected}"', tags=['bdd'])
    def result_should_be_expected(self, expected):
        self.result_should_be(expected)
