import argparse

import database as db
from constants import ERROR_MESSAGE, DNA_BASES


def convert_dna_to_rna(dna: str) -> str:
    """ Function that imitates the transcription process """

    if is_incorrect_input(dna):
        return ERROR_MESSAGE

    rna = ''
    with db.Session() as session:
        for base in dna:
            query = session.query(db.Dna).join(db.Rna)
            entry = query.filter(db.Dna.dna_base == base).one()
            rna += str(entry.rna_base)
    return rna


def is_incorrect_input(input_dna: str) -> bool:
    """ Checks if the input is a correct DNA sequence """

    str_input = str(input_dna)
    not_bases = len(set(str_input) - DNA_BASES) != 0
    not_string = not isinstance(input_dna, str)

    return not_bases or not_string


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='DNA to RNA converter',
                                     fromfile_prefix_chars='@')
    parser.add_argument('dna', help='DNA sequence')
    arg = parser.parse_args()
    rna = convert_dna_to_rna(arg.dna)
    with open("data/outputs/output_rna_sequence.txt", "w") as output:
        output.write(rna)
    print(rna)
