import unittest
import biblioteca

class TestComplejos(unittest.TestCase):

    def test_suma_1(self):
        self.assertEqual(biblioteca.sumaCplx((2, -1), (-1, 3)), (1, 2))

    def test_suma_2(self):
        self.assertEqual(biblioteca.sumaCplx((0, 0), (3, 4)), (3, 4))

    def test_resta_1(self):
        self.assertEqual(biblioteca.restaCplx((2, -1), (-1, 3)), (3, -4))

    def test_resta_2(self):
        self.assertEqual(biblioteca.restaCplx((5, 5), (2, 3)), (3, 2))

    def test_producto_1(self):
        self.assertEqual(biblioteca.prodCplx((2, -1), (-1, 3)), (1, 7))

    def test_producto_2(self):
        self.assertEqual(biblioteca.prodCplx((1, 1), (1, -1)), (2, 0))

    def test_division_1(self):
        self.assertEqual(biblioteca.divisionCplx((2, -1), (-1, 3)), (-0.5, -0.5))

    def test_division_2(self):
        self.assertEqual(biblioteca.divisionCplx((1, 1), (1, 1)), (1.0, 0.0))

    def test_modulo_1(self):
        self.assertEqual(biblioteca.moduloClpx((3, 4)), 5.0)

    def test_modulo_2(self):
        self.assertEqual(biblioteca.moduloClpx((0, 0)), 0.0)

    def test_conjugado_1(self):
        self.assertEqual(biblioteca.conjugadoClpx((2, -1)), (2, 1))

    def test_conjugado_2(self):
        self.assertEqual(biblioteca.conjugadoClpx((3, 4)), (3, -4))

    def test_polar_a_cartesiano_1(self):
        self.assertEqual(biblioteca.conversionPolarCartesianoClpx((1, 0)), (1.0, 0.0))

    def test_polar_a_cartesiano_2(self):
        self.assertEqual(biblioteca.conversionPolarCartesianoClpx((2, 0)), (2.0, 0.0))

    def test_cartesiano_a_polar_1(self):
        self.assertEqual(biblioteca.conversionCartesianoPolarClpx((3, 4)), (5.0, 0.93))

    def test_cartesiano_a_polar_2(self):
        self.assertEqual(biblioteca.conversionCartesianoPolarClpx((1, 0)), (1.0, 0.0))

    def test_fase_1(self):
        self.assertAlmostEqual(biblioteca.faseClpx((1, 1)), 0.79, places=2)

    def test_fase_2(self):
        self.assertAlmostEqual(biblioteca.faseClpx((0, 1)), 1.57, places=2)

if __name__ == "__main__":
    unittest.main()
