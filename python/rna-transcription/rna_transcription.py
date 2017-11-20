import re

def to_rna(dna_strand):
    if not re.search('^[GCTA]+$', dna_strand):
        raise ValueError

    # DNA to placeholder
    dna_strand = dna_strand.replace('G', '1')
    dna_strand = dna_strand.replace('C', '2')
    dna_strand = dna_strand.replace('T', '3')
    dna_strand = dna_strand.replace('A', '4')

    # placeholder to RNA
    dna_strand = dna_strand.replace('1', 'C')
    dna_strand = dna_strand.replace('2', 'G')
    dna_strand = dna_strand.replace('3', 'A')
    dna_strand = dna_strand.replace('4', 'U')

    return dna_strand
