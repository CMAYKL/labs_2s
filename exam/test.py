import unittest
from main import generate_list

class TestGenerateList(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(generate_list(5), [0, 1, 2, 3, 4])

if __name__ == "__main__":
    unittest.main()
