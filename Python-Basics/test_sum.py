import unittest
import testing as t


class MyTestCase(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(t.positive_sum([1, 2, 3]), 6)  # test if sum works
        self.assertRaises(ValueError, t.positive_sum, [-1, 3, 6])  # test if exception raises
        self.assertRaises(TypeError, t.positive_sum, 3)


if __name__ == '__main__':
    unittest.main()
