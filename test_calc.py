## Unittest for Calc class
import unittest

from stack import Stack
from calc import Calc


class CalcTest(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(Calc.eval("2 5 +"), 7)
        self.assertEqual(Calc.eval("-250.3 100 +"), -150.3) # Negative number test
        self.assertEqual(Calc.eval("2 5 + 3 + -4 + 2 2 + +"), 10) # Addition sequence test

    def test_subtraction(self):
        self.assertEqual(Calc.eval("8 5 -"), 3)
        self.assertEqual(Calc.eval("-3 5 -"), -8) # Negative number test
        self.assertEqual(Calc.eval("-3 7 - -17 - 2 2 - -"), 7) # Subtraction sequence test

    def test_multiplication(self):
        self.assertEqual(Calc.eval("8 4 *"), 32)
        self.assertEqual(Calc.eval("52 3 *"), 156)
        self.assertEqual(Calc.eval("3 -3 *"), -9) # Negative Number test
        self.assertEqual(Calc.eval("3 -3 * -2 * 1 2 * *"), 36) # Multiplication sequence test

    def test_division(self):
        self.assertEqual(Calc.eval("5 2 /"), 2.5)
        self.assertEqual(Calc.eval("5 2 / 2.5 /"), 1) # Division sequence test
        self.assertEqual(Calc.eval("5 2 / -2.5 / -5 -5 / /"), -1) # Negative number test

    def test_division_byZero(self):
        with self.assertRaises(ZeroDivisionError):
            Calc.eval("5 0 /")

        with self.assertRaises(ZeroDivisionError):
            Calc.eval("4 2 - 2 2 - /")

    def test_illegal_expressionType(self):
        with self.assertRaises(Exception, msg = "Input should be a string (RPN format)!"):
            Calc.eval(2 + 3)

    def test_illegal_expressionInput(self):
        with self.assertRaises(Exception, msg = "Stack size in the end not equal to 1! Please correct input!"):
            Calc.eval("2 5 + 3 + 7")

    def test_sequence(self):
        self.assertEqual(Calc.eval("2 -3 * 5 + -99 - 2 + 2 / 25 2 * /"), 1)
