import unittest
import biblioteca

class TestComplejos(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(
            biblioteca.sumaCplx((2, -1), (-1, 3)),
            (1, 2)
        )

    def test_resta(self):
        self.assertEqual(
            biblioteca.restaCplx((2, -1), (-1, 3)),
            (3, -4)
        )

    def test_producto(self):
        self.assertEqual(
            biblioteca.prodCplx((2, -1), (-1, 3)),
            (1, 7)
        )

    def test_division(self):
        self.assertEqual(
            biblioteca.divisionCplx((2, -1), (-1, 3)),
            (-0.5, -0.5)
        )

    def test_modulo(self):
        self.assertEqual(
            biblioteca.moduloClpx((3, 4)),
            5.0
        )

    def test_conjugado(self):
        self.assertEqual(
            biblioteca.conjugadoClpx((2, -1)),
            (2, 1)
        )

    def test_fase(self):
        self.assertAlmostEqual(
            biblioteca.faseClpx((1, 1)),
            0.79,
            places=2
        )

if __name__ == "__main__":
    unittest.main()
