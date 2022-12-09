import unittest
from parameterized import parameterized

from convert_rna_to_protein import convert_rna_to_protein
from constants import ERROR_MESSAGE


class TestConvertRnaToProtein(unittest.TestCase):

    @parameterized.expand([
        ("basic", "AUUUGGCUACUAACAAUCUA", "IWLLTI"),
        ("with_stop_codon", "GCUAACUAACAUCUUUGGCACUGUU", "AN.HLWHC"),
        ("less_than_codon", "GC", ""),
        ("empty", "", ""),
    ])
    def test_basic(self, _, rna, protein):
        """ Tests basic cases """

        expected = protein
        actual = convert_rna_to_protein(rna)
        self.assertTrue(expected == actual, f"Should be {protein}")

    @parameterized.expand([
        ("not_upper_case", "aAggc", ERROR_MESSAGE),
        ("not_bases", "GGAYT", ERROR_MESSAGE),
        ("not_string", 987, ERROR_MESSAGE),
    ])
    def test_incorrect_input(self, _, dna, error_msg):
        """ Tests if the input is incorrect """

        expected = error_msg
        actual = convert_rna_to_protein(dna)
        self.assertTrue(expected == actual, "Should throw an error message")


if __name__ == '__main__':
    unittest.main()
