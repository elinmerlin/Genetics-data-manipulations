import unittest
from parameterized import parameterized

from convert_dna_to_rna import convert_dna_to_rna
from constants import ERROR_MESSAGE


class TestConvertDnaToRna(unittest.TestCase):

    @parameterized.expand([
        ("basic", "ATTTGGCTACTAACAATCTA", "AUUUGGCUACUAACAAUCUA"),
        ("empty", "", ""),
    ])
    def test_basic(self, _, dna, rna):
        """ Tests basic cases """

        expected = rna
        actual = convert_dna_to_rna(dna)
        self.assertTrue(expected == actual, f"Should be {rna}")

    @parameterized.expand([
        ("not_upper_case", "aAggc", ERROR_MESSAGE),
        ("not_bases", "GGAYT", ERROR_MESSAGE),
        ("not_string", 987, ERROR_MESSAGE),
    ])
    def test_incorrect_input(self, _, dna, error_msg):
        """ Tests if the input is incorrect """

        expected = error_msg
        actual = convert_dna_to_rna(dna)
        self.assertTrue(expected == actual, "Should throw an error message")


if __name__ == '__main__':
    unittest.main()
