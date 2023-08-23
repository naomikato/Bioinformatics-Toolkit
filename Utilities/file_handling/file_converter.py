#!/usr/bin/env python
import os

def convert_fasta_to_fastq(input_fasta, output_fastq):
    """
    Convert a FASTA file to FASTQ format by adding dummy quality scores.
    """
    with open(input_fasta, "r") as fasta_file, open(output_fastq, "w") as fastq_file:
        for line in fasta_file:
            if line.startswith(">"):
                header = line.strip()
                sequence = next(fasta_file).strip()
                quality_scores = "I" * len(sequence)
                fastq_file.write(f"{header}\n{sequence}\n+\n{quality_scores}\n")

def main():
    input_fasta = "input.fasta"
    output_fastq = "output.fastq"
    
    print("Converting FASTA to FASTQ")
    convert_fasta_to_fastq(input_fasta, output_fastq)
    print("Conversion completed. FASTQ file saved as", output_fastq)

if __name__ == "__main__":
    main()
