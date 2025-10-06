import unittest
from operations import additionOperation, subtrationOperation, multiplicationOperation


class TestMathFunctions(unittest.TestCase):

    def testAdditionOperation(self):
        mathAditionResult = additionOperation(num1=5, num2=15)
        self.assertEqual(mathAditionResult, 20)

    def testSubtractionOperation(self):
        mathSubtractionResult = subtrationOperation(num1=5, num2=15)
        self.assertEqual(mathSubtractionResult, -10)

    def testMultiplicationOperation(self):
        mathMultiplicationResult = multiplicationOperation(num1=5, num2=15)
        self.assertEqual(mathMultiplicationResult, 75)


if __name__ == '__main__':
    unittest.main()
