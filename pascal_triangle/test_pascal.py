import unittest
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle


class TestPascal(unittest.TestCase):
    def test_pascal(self):
        self.assertEqual(len(pascal_triangle(5)), 5)
        self.assertEqual(pascal_triangle(5), [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])


if __name__ == '__main__':
    unittest.main()
