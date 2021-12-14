## Unittest for Stack class
import unittest

from stack import Stack


class StackTest(unittest.TestCase):

    def test_push(self):
        s = Stack()
        s.push(4), s.push(7), s.push(8)
        self.assertEqual(s.container[-1], 8)
        self.assertTrue(len(s.container) == 3, "3 times push must lead to lenth of container == 3")
        self.assertIn(4, s.container)

    def test_getSize_empty(self):
        s = Stack()
        self.assertTrue(s.getSize() == 0, "Container should be empty")

    def test_getSize_nonEmpty(self):
        s = Stack()
        s.push(4), s.push(7), s.push(8)
        self.assertTrue(s.getSize() == 3, "Container should have length 3")


    def test_pop_empty(self):
        s = Stack()
        with self.assertRaises(Exception, msg = "Can't pop from an empty stack. Please push elements first!"):
            s.pop()


    def test_pop_nonEmpty(self):
        s = Stack()
        s.push(4), s.push(7), s.push(8)
        self.assertEqual(s.pop(), 8)
        self.assertTrue(len(s.container) == 2, "obj.pop() should remove last item (LIFO)")


    def test_peek_empty(self):
        s = Stack()
        with self.assertRaises(Exception, msg = "Cant show last element of the stack because there are no elements!"):
            s.peek()


    def test_peek_nonEmpty(self):
        s = Stack()
        s.push(4), s.push(7), s.push(8)
        self.assertEqual(s.peek(), 8)


    def test_sequence(self):
        s = Stack()
        s.push(20), s.push(2), s.push(30)
        s.pop(), s.pop()
        self.assertEqual(len(s.container), 1)
        self.assertTrue(s.peek() == 20)
        s.push(4)
        self.assertTrue(s.getSize() == 2)
        s.pop()
        self.assertEqual(s.pop(), 20)
        with self.assertRaises(Exception):
            s.peek()

