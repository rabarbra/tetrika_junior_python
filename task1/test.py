import unittest
from task import task

class TaskTestCase(unittest.TestCase):
    def test_no_zero(self):
        self.assertRaises(ValueError, task, "")
        self.assertRaises(ValueError, task, "1")
        self.assertRaises(ValueError, task, "11")
        self.assertRaises(ValueError, task, "111")
        self.assertRaises(ValueError, task, "11111111111")

    def test_no_one(self):
        self.assertEqual(task("0"), 0)
        self.assertEqual(task("00"), 0)
        self.assertEqual(task("000"), 0)
        self.assertEqual(task("0000000000000000000000000000000"), 0)

    def test_one_zero(self):
        self.assertEqual(task("10"), 1)
        self.assertEqual(task("110"), 2)
        self.assertEqual(task("1110"), 3)
        self.assertEqual(task("111111111111111111110"), 20)

    def test_more_zeros(self):
        self.assertEqual(task("100"), 1)
        self.assertEqual(task("1000"), 1)
        self.assertEqual(task("1000000000000000000000"), 1)
        self.assertEqual(task("1100"), 2)
        self.assertEqual(task("110000000000000000"), 2)
        self.assertEqual(task("111111111111111111111111100"), 25)
        self.assertEqual(task("11111111111111111111111110000"), 25)
        self.assertEqual(task("1111111111111111111111111000000000000000000000000000"), 25)

if __name__ == "__main__":
    unittest.main()
