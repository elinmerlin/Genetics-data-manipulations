import argparse

import matplotlib.pyplot as plt
import numpy as np

from constants import ERROR_MESSAGE, DNA_BASES


def plot_the_gc_ratio(sequence: str, name: str, step: int = 100) -> str:
    """ Function that plots the GC-content graph """
    if is_incorrect_input(sequence):
        return ERROR_MESSAGE

    step = min(len(sequence), step)
    ratios = []
    start, end = 0, step
    bases_number = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    while end <= len(sequence):
        bases_number.update({'A': 0, 'T': 0, 'G': 0, 'C': 0})
        for base in sequence[start:end]:
            bases_number[base] += 1
        ratio = ((bases_number['G'] + bases_number['C']) / step) * 100
        ratios.append(ratio)
        start += step
        end += step
    ratios.append(ratios[-1])
    x = np.arange(0, len(sequence) + 1, step)
    plt.step(x, ratios, where='post')
    plt.suptitle('GC content distribution')
    plt.ylabel('guanine-cytosine ratio (%)')
    plt.xlabel('DNA bases position')
    plt.savefig(f'/app/data/outputs/gc-content-graphs/{name}.png')
    return 'The graph is stored'


def is_incorrect_input(input_dna: str) -> bool:
    """ Checks if the input is a correct DNA sequence """

    str_input = str(input_dna)
    is_empty = len(str_input) == 0
    not_bases = len(set(str_input) - DNA_BASES) != 0
    not_string = not isinstance(input_dna, str)

    return not_bases or not_string or is_empty


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot the gc-content graph',
                                     fromfile_prefix_chars='@')
    parser.add_argument('sequence', help='DNA sequence')
    parser.add_argument('-s', '--step', type=int,
                        required=False, default=100, help='DNA sequence')
    parser.add_argument('name', help='Graph name')
    arg = parser.parse_args()
    response = plot_the_gc_ratio(arg.sequence, arg.name, step=arg.step)
    print(response)
