import unittest
from unittest.mock import patch
from parameterized import parameterized

from plot_the_gc_ratio import plot_the_gc_ratio
from constants import ERROR_MESSAGE


class TestPlotTheGcRatio(unittest.TestCase):

    @parameterized.expand([
        ("basic", "GCGGCCAACTAACATCTTGCG", 10, "test1"),
        ("large_step", "GCGCGCGCAAAAGCGC", 100, "test2"),
    ])
    def test_basic(self, _, dna, step, name):
        """ Tests if the function creates a png file """

        with patch('plot_the_gc_ratio.plt.savefig') as mock:
            plot_the_gc_ratio(dna, name, step=step)
            mock.assert_called()

    @parameterized.expand([
        ("not_upper_case", "aAggc", ERROR_MESSAGE, "test3"),
        ("not_bases", "GGAYT", ERROR_MESSAGE, "test4"),
        ("not_string", 987, ERROR_MESSAGE, "test5"),
        ("empty", "", ERROR_MESSAGE, "test6"),
    ])
    def test_incorrect_input(self, _, dna, error_msg, name):
        """ Tests if the input is incorrect """

        expected = error_msg
        actual = plot_the_gc_ratio(dna, name)
        self.assertTrue(expected == actual, "Should throw an error message")


if __name__ == '__main__':
    unittest.main()
