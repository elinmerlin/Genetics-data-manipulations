import argparse

import database as db
from constants import CODON_LENGTH, ERROR_MESSAGE, RNA_BASES


def convert_rna_to_protein(rna: str) -> str:
    """ Function that imitates the translation process """

    if is_incorrect_input(rna):
        return ERROR_MESSAGE

    start, end = 0, CODON_LENGTH
    polypeptide = ''
    with db.Session() as session:
        while end <= len(rna):
            codon = rna[start:end]
            query = session.query(db.Triplets).join(db.AminoAcids)
            entry = query.filter(db.Triplets.codon == codon).one()
            polypeptide += str(entry.aminoacid)
            start += CODON_LENGTH
            end += CODON_LENGTH
    return polypeptide


def is_incorrect_input(input_rna: str) -> bool:
    """ Checks if the input is a correct RNA sequence """

    str_input = str(input_rna)
    not_bases = len(set(str_input) - RNA_BASES) != 0
    not_string = not isinstance(input_rna, str)

    return not_bases or not_string


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='RNA to polypeptide converter',
                                     fromfile_prefix_chars='@')
    parser.add_argument('rna', help='RNA sequence')
    arg = parser.parse_args()
    polypeptide = convert_rna_to_protein(arg.rna)
    with open("data/outputs/output_polypeptide.txt", "w") as output:
        output.write(polypeptide)
    print(polypeptide)
