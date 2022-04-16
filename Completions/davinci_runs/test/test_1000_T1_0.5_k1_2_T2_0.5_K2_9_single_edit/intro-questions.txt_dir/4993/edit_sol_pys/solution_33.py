
import os
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna


def find_in_seq(seq, motif):
    for i in range(len(seq)):
        if seq[i:i + len(motif)] == motif:
            return i
    return -1


def find_in_seqrecord(seqrecord, motif):
    return find_in_seq(str(seqrecord.seq), motif)


def find_in_fasta(fasta, motif):
    for record in SeqIO.parse(fasta, "fasta"):
        index = find_in_seqrecord(record, motif)
        if index > -1:
            return record.id, index
    return None, None


def find_in_genbank(genbank, motif):
    for record in SeqIO.parse(genbank, "genbank"):
        index = find_in_seqrecord(record, motif)
        if index > -1:
            return record.id, index
    return None, None


def find_in_gbk(gbk, motif):
    return find_in_genbank(gbk, motif)


def find_in_gb(gbk, motif):
    return find_in_genbank(gbk, motif)


def find_in_embl(embl, motif):
    for record in SeqIO.parse(embl, "embl"):
        index = find_in_seqrecord(record, motif)
        if index > -1:
            return record.id, index
    return None, None


def find_in_fastq(fastq, motif):
    for record in SeqIO.parse(fastq, "fastq"):
        index = find_in_seqrecord(record, motif)
        if index > -1:
            return record.id, index
    return None, None


def find_in_fastq_sanger(fastq, motif):
    for record in SeqIO.parse(fastq, "fastq-sanger"):
        index = find_in_seqrecord(record, motif)
        if index > -1:
            return record.id, index
    return None, None


def find_in_fastq_solexa(fastq, motif):
    for record in SeqIO.parse(fastq, "fastq-solexa"):
        index = find_in_seqrecord(record, motif)
        if index > -1:
            return record.id, index
    return None, None


def find_in_fastq_illumina(fastq, motif):
    for record in SeqIO.parse(fastq, "fastq-illumina"):
        index = find_in_seqrecord(record, motif)
        if index > -1:
            return record.id, index
    return None, None


def find_in_phd(phd, motif):
    for record in SeqIO.parse(phd, "phd"):
        index = find_in_seqrecord(record, motif)
        if index > -1:
            return record.id, index
    return None, None


def find_in_qual(qual, motif):
    for record in SeqIO.parse(qual, "qual"):
        index = find_in_seqrecord(record, motif)
        if index > -1:
            return record.id, index
    return None, None


def find_in_sff(sff, motif):
    for record in SeqIO.parse(sff, "sff"):
        index = find_in_seqrecord(record, motif)
        if index > -1:
            return record.id, index
    return None, None


def find_in_uniprot_xml(uniprot_xml, motif):
    for record in SeqIO.parse(uniprot_xml, "uniprot-xml"):
        index = find_in_seqrecord(record, motif)
        if index > -1:
            return record.id, index
    return None, None


def find_in_uniprot_txt(uniprot_txt, motif):
    for record in SeqIO.parse(uniprot_txt, "uniprot-txt"):
        index = find_in_seqrecord(record, motif)
        if index > -1:
            return record.id, index
    return None, None


def find_in_nexus(nexus, motif):
    for record in SeqIO.parse(nexus, "nexus"):
        index = find_in_seqrecord(record, motif)
        if index > -1:
            return record.id, index
    return None, None


def find_in_clustal(clustal, motif):
    for record in SeqIO.parse(clustal, "clustal"):
        index = find_in_seqrecord(record, motif)
        if index > -1:
            return record.id, index
    return None, None


def find_in_stockholm(stockholm, motif):
    for record in SeqIO.parse(stockholm, "stockholm"):
        index = find_in_seqrecord(record, motif)
        if index > -1:
            return record.id, index
    return None, None


def find_in_pir(pir, motif):
    for record in SeqIO.parse(pir, "pir"):
        index = find_in_seqrecord(record, motif)
        if index > -1:
            return record.id, index
    return None, None


def find_in_tab(tab, motif):
    for record in SeqIO.parse(tab, "tab"):
        index = find_in_seqrecord(record, motif)
        if index > -1:
            return record.id, index
    return None, None


def main():
    pass


if __name__ == "__main__":
    main()
