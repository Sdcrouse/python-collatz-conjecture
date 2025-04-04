import unittest

from collatz.collatz_conjecture import collatz, get_next_number

class TestCollatzConjecture(unittest.TestCase):
    
    def test_collatz_string(self):
        collatz_number = 1
        expected_collatz_string = '1 -> 4 -> 2 -> 1'
        self.assertEqual(expected_collatz_string, collatz(collatz_number))

        collatz_number = 4
        expected_collatz_string = '4 -> 2 -> 1'
        self.assertEqual(expected_collatz_string, collatz(collatz_number))

        collatz_number = 6
        expected_collatz_string = '6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1'
        self.assertEqual(expected_collatz_string, collatz(collatz_number))

    def test_collatz_string_parts(self):
        collatz_number = 5
        collatz_string = collatz(collatz_number)

        self.assertEqual('5', collatz_string[0], 'Generated Collatz string should start with the original number')
        self.assertEqual('1', collatz_string[-1], 'Generated Collatz string should end with 1')

    def test_get_next_number(self):
        even_collatz_number = 8
        self.assertEqual(4, get_next_number(even_collatz_number), 'When the number is even, divide it by 2')

        odd_collatz_number = 5
        self.assertEqual(16, get_next_number(odd_collatz_number), 'When the number is odd, multiply it by 3 and add 1')

if __name__ == '__main__':
    unittest.main()