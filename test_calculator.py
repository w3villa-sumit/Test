import unittest
from calculator import add, subtract


class TestCalculator(unittest.TestCase):

    def test_add_valid_numbers(self):
        # Normal and edge cases
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(0, 0), 0)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=1)  # floating precision

    def test_add_invalid_inputs(self):
        # Should raise TypeError for non-numeric inputs
        with self.assertRaises(TypeError):
            add("2", 3)
        with self.assertRaises(TypeError):
            add(None, 5)

    def test_subtract_valid_numbers(self):
        # Normal and edge cases
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-3, -2), -1)
        self.assertAlmostEqual(subtract(0.3, 0.1), 0.2, places=1)

    def test_subtract_invalid_inputs(self):
        # Should raise TypeError for non-numeric inputs
        with self.assertRaises(TypeError):
            subtract(10, "5")
        with self.assertRaises(TypeError):
            subtract("x", "y")


if __name__ == "__main__":
    unittest.main()
