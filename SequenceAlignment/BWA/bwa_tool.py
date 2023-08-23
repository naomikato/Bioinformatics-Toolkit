#!/usr/bin/env python
import subprocess
import os

def run_bwa(input_fastq, reference_genome, output_sam):
    """
    Run BWA to align input FASTQ reads to the reference genome and save the alignment in SAM format.
    """
    command = ["bwa", "mem", reference_genome, input_fastq]
    with open(output_sam, "w") as sam_file:
        subprocess.run(command, stdout=sam_file, check=True)

def main():
    input_fastq = "sample_reads.fastq"
    reference_genome = "reference_genome.fa"
    output_sam = "aligned_reads.sam"
    
    print("Aligning reads using BWA")
    run_bwa(input_fastq, reference_genome, output_sam)
    print("Alignment completed. SAM file saved as", output_sam)

if __name__ == "__main__":
    main()
