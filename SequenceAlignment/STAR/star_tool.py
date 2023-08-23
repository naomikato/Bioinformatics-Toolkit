#!/usr/bin/env python
import subprocess
import os

def run_star(input_fastq, reference_genome_dir, output_dir):
    """
    Run STAR to align input RNA-seq FASTQ reads to the reference genome and save the aligned output.
    """
    command = [
        "STAR", "--runThreadN", "4", "--genomeDir", reference_genome_dir,
        "--readFilesIn", input_fastq, "--outFileNamePrefix", output_dir
    ]
    subprocess.run(command, check=True)

def main():
    input_fastq = "rna_seq_reads.fastq"
    reference_genome_dir = "reference_genome_directory"
    output_dir = "alignment_output"
    
    print("Aligning RNA-seq reads using STAR")
    run_star(input_fastq, reference_genome_dir, output_dir)
    print("Alignment completed. Aligned output saved in", output_dir)

if __name__ == "__main__":
    main()
