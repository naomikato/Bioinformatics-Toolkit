#!/usr/bin/env python
import subprocess
import os

def run_fastqc(input_fastq, output_dir):
    """
    Run FastQC on the input FASTQ file and save results in the output directory.
    """
    command = ["fastqc", input_fastq, "-o", output_dir]
    subprocess.run(command, check=True)

def main():
    input_fastq = "sample_data.fastq"
    output_dir = "fastqc_results"
    
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    print("Running FastQC on", input_fastq)
    run_fastqc(input_fastq, output_dir)
    print("FastQC completed. Results saved in", output_dir)

if __name__ == "__main__":
    main()
