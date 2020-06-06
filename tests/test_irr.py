import unittest
from petrolpy_equations import petrolpy_equations


class Equations_Test(unittest.TestCase):

    """Validate using CFI example:

    https://corporatefinanceinstitute.com/resources/knowledge/finance/internal-rate-return-irr/

    IRR in example is 13% but given the function rounding method it results in 14%
    """

    def test_irr(self):
        values = [-500_000, 160_000, 160_000, 160_000, 160_000, 50_000]

        irr = petrolpy_equations.irr(values)
        self.assertEqual(irr, 0.14)


if __name__ == "__main__":
    unittest.main()
