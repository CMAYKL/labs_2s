
import unittest
from app import Figure  # імпортуємо клас Figure з файлу app.py

class TestFigure(unittest.TestCase):

    def test_square_area(self):
        fig = Figure("квадрат", 5)
        self.assertEqual(fig.area(), 25)

    def test_square_perimeter(self):
        fig = Figure("квадрат", 5)
        self.assertEqual(fig.perimeter(), 20)

    def test_rectangle_area(self):
        fig = Figure("прямокутник", 5, 10)
        self.assertEqual(fig.area(), 50)

    def test_rectangle_perimeter(self):
        fig = Figure("прямокутник", 5, 10)
        self.assertEqual(fig.perimeter(), 30)

    def test_triangle_area(self):
        fig = Figure("трикутник", 5)
        self.assertEqual(fig.area(), 12.5)

    def test_triangle_perimeter(self):
        fig = Figure("трикутник", 5)
        self.assertEqual(fig.perimeter(), 15)

    def test_invalid_figure_type(self):
        with self.assertRaises(AssertionError):
            Figure("коло", 5)

    def test_invalid_length(self):
        with self.assertRaises(AssertionError):
            Figure("квадрат", -5)

            
    def test_get_angles():
        """Тестуємо чи правильно повертається кількість кутів фігури.
        """
        fig = "трикутник"
        triangle = Figure(fig, 1)
        assert triangle.get_angles == 3, f"У {fig} є 3 кути!"

if __name__ == "__main__":
    unittest.main()
