## Implementing stack based calculator (static class)

from stack import Stack

class Calc:

    def __init__(self):
        pass

    @staticmethod
    def eval(expression):
        if isinstance(expression, str) == False:
            raise Exception("Input should be a string (RPN format)!")
        expression = expression.split()
        stack = Stack()
        for exp in expression:

            if exp in ["+", "-", "*", "/"]:
                a = stack.pop()
                b = stack.pop()
                if exp == "*":
                    stack.push(a*b)

                if exp == "+":
                    stack.push(a+b)

                if exp == "-":
                    stack.push(b-a)

                if exp == "/":
                    stack.push(b/a)
            else:
                stack.push(float(exp))

        if stack.getSize() != 1:
            raise Exception("Stack size in the end not equal to 1! Please correct input!")
        else:
            return stack.peek()
