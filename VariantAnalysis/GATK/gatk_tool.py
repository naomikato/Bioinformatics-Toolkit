#!/usr/bin/env python
import subprocess
import os

def run_gatk(input_bam, reference_genome, output_vcf):
    """
    Run GATK to call variants from the input BAM file and save the variant calls in VCF format.
    """
    command = [
        "gatk", "HaplotypeCaller", "-R", reference_genome, "-I", input_bam, "-O", output_vcf
    ]
    subprocess.run(command, check=True)

def main():
    input_bam = "aligned_reads.bam"
    reference_genome = "reference_genome.fa"
    output_vcf = "variant_calls.vcf"
    
    print("Calling variants using GATK")
    run_gatk(input_bam, reference_genome, output_vcf)
    print("Variant calling completed. Variant calls saved in", output_vcf)

if __name__ == "__main__":
    main()
