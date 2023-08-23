#!/usr/bin/env python
import subprocess
import os

def run_trimmomatic(input_fastq, output_fastq, adapters_file):
    """
    Run Trimmomatic on the input FASTQ file, using the specified adapters file, and save the trimmed output.
    """
    command = ["trimmomatic", "SE", input_fastq, output_fastq, "ILLUMINACLIP:" + adapters_file + ":2:30:10"]
    subprocess.run(command, check=True)

def main():
    input_fastq = "input_data.fastq"
    output_fastq = "output_data_trimmed.fastq"
    adapters_file = "adapters.fa"
    
    print("Running Trimmomatic on", input_fastq)
    run_trimmomatic(input_fastq, output_fastq, adapters_file)
    print("Trimmomatic completed. Trimmed output saved in", output_fastq)

if __name__ == "__main__":
    main()
