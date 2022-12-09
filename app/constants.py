
CODON_LENGTH = 3

CODONS_AMINOACIDS_MAP = {
    'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'G': ['GGU', 'GGC', 'GGA', 'GGG'],
    'M': ['AUG'],
    'S': ['AGU', 'AGC', 'UCU', 'UCC', 'UCA', 'UCG'],
    'C': ['UGU', 'UGC'],
    'H': ['CAU', 'CAC'],
    'N': ['AAU', 'AAC'],
    'T': ['ACU', 'ACC', 'ACA', 'ACG'],
    'D': ['GAU', 'GAC'],
    'I': ['AUU', 'AUC', 'AUA'],
    'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    'V': ['GUU', 'GUC', 'GUA', 'GUG'],
    'E': ['GAA', 'GAG'],
    'K': ['AAA', 'AAG'],
    'Q': ['CAA', 'CAG'],
    'W': ['UGG'],
    'F': ['UUU', 'UUC'],
    'L': ['CUU', 'CUC', 'CUA', 'CUG', 'UUA', 'UUG'],
    'R': ['AGA', 'AGG', 'CGU', 'CGC', 'CGA', 'CGG'],
    'Y': ['UAU', 'UAC'],
    '.': ['UAA', 'UAG', 'UGA']
}

DNA_BASES = {'A', 'T', 'G', 'C'}

RNA_BASES = {'A', 'U', 'G', 'C'}

ERROR_MESSAGE = 'Something went wrong. Try again.'
