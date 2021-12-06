#  test_main -> file name
# in Here test_Calculator
import unittest
from Calculator import Calculator


class TestCalculator(unittest.TestCase):
    # now this instance are class property and usable all over the class
    # it runs at first before each methode
    def setUp(self) -> None:
        print("i hope it runs fine")
        self.c1 = Calculator()
        self.c2 = Calculator()

    @classmethod
    def setUpClass(cls) -> None:
        print("it runs only once at the beginning")

    @classmethod
    def tearDownClass(cls) -> None:
        print("it runs only once at the End.....!")

    # it runs after each methode
    def tearDown(self) -> None:
        print("this test was successfully")

    # function test must be start with test like sample
    def test_sum(self):
        print("test_sum")
        self.assertEqual(Calculator.sum(1, 2, 3), 6)
        self.assertEqual(Calculator.sum(-1, 1), 0)

    def test_pow(self):
        print("test_pow")
        self.assertEqual(Calculator.power(4, 1/2), 2)
        self.assertEqual(Calculator.power(2, 0), 1)
        self.assertEqual(Calculator.power(2, 10), 1024)

    def test_fac(self):
        print("test_fac")
        self.assertEqual(Calculator.fac(1), 1)
        self.assertEqual(Calculator.fac(0), 1)
        self.assertEqual(Calculator.fac(3), 6)


if __name__ == '__main__':
    unittest.main()
