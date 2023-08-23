#!/usr/bin/env python
import subprocess
import os

def run_bcftools(input_vcf, output_filtered_vcf):
    """
    Run bcftools to filter variants in the input VCF file and save the filtered variants in a new VCF file.
    """
    command = ["bcftools", "view", "-f", "PASS", "-o", output_filtered_vcf, "-O", "v", input_vcf]
    subprocess.run(command, check=True)

def main():
    input_vcf = "variant_calls.vcf"
    output_filtered_vcf = "filtered_variants.vcf"
    
    print("Filtering variants using bcftools")
    run_bcftools(input_vcf, output_filtered_vcf)
    print("Variant filtering completed. Filtered variants saved in", output_filtered_vcf)

if __name__ == "__main__":
    main()
