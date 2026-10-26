import unittest
from roman import convert

class TestRomanConverter(unittest.TestCase):
    
    # Standard valid cases
    def test_additive_notation(self):
        self.assertEqual(convert("I"), 1)
        self.assertEqual(convert("V"), 5)
        self.assertEqual(convert("III"), 3)
        self.assertEqual(convert("XVI"), 16)

    def test_subtractive_notation(self):
        self.assertEqual(convert("IV"), 4)
        self.assertEqual(convert("IX"), 9)
        self.assertEqual(convert("XL"), 40)
        self.assertEqual(convert("XC"), 90)

    def test_combined_notation(self):
        self.assertEqual(convert("XIX"), 19)

    # Invalid character & subtractive checks
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            convert("ABC")
        with self.assertRaises(ValueError):
            convert("VX")

    # Edge cases: Invalid repetition checks
    def test_invalid_repetitions(self):
        # Non-repeatable symbols (V, L, D) cannot repeat twice
        with self.assertRaises(ValueError):
            convert("VV")
        with self.assertRaises(ValueError):
            convert("LL")
        with self.assertRaises(ValueError):
            convert("DD")
            
        # Repeatable symbols (I, X, C, M) cannot repeat 4 times
        with self.assertRaises(ValueError):
            convert("IIII")
        with self.assertRaises(ValueError):
            convert("XXXX")

if __name__ == "__main__":
    unittest.main()