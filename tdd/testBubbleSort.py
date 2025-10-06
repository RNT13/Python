import unittest

from sort import bubbleSort


class TestBubbleSort(unittest.TestCase):
    def testBubbleSort(self):
        unsortedList = [64, 34, 25, 12, 22, 11, 90]
        sortedList = [11, 12, 22, 25, 34, 64, 90]

        unsortedList = bubbleSort(unsortedList)
        self.assertEqual(unsortedList, unsortedList)

        print(unsortedList)
        print('list sorted')


if __name__ == '__main__':
    unittest.main()
