
import os
import csv
from jiwer import wer, cer, mer, wil


def read_from_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        text = ''.join(lines)
        return text


def process_folder(reference_folder, hypothesis_folder_1, hypothesis_folder_2, output_csv):
    # Open the CSV file in write mode
    with open(output_csv, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['FileName', 'WER_IBM_Watson', 'WER_WhisperX', 'CER_IBM_Watson',
                      'CER_WhisperX', 'MER_IBM_Watson', 'MER_WhisperX', 'WIL_IBM_Watson', 'WIL_WhisperX']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        # Iterate over files in the reference folder
        for ref_file in os.listdir(reference_folder):
            if ref_file.endswith('.txt'):  # Ensure it's a text file
                # Extract the number part from the reference file name
                # Assuming the format is C<number>-ref.txt
                ref_number = ref_file.split('-')[0]

                # Construct the hypothesis file names based on the number
                hypo_file_1 = f"{ref_number}-hypo-ibm-n.txt"  # IBM Watson
                hypo_file_2 = f"{ref_number}-hypo-w-n.txt"  # WhisperX

                # Construct full file paths
                ref_path = os.path.join(reference_folder, ref_file)
                hypo_path_1 = os.path.join(hypothesis_folder_1, hypo_file_1)
                hypo_path_2 = os.path.join(hypothesis_folder_2, hypo_file_2)

                # Check if both hypothesis files exist
                if os.path.exists(hypo_path_1) and os.path.exists(hypo_path_2):
                    # Read the reference text
                    reference = read_from_file(ref_path)

                    # Read both hypothesis texts
                    hypothesis_1 = read_from_file(hypo_path_1)
                    hypothesis_2 = read_from_file(hypo_path_2)

                    # Calculate the error rates for the first hypothesis (IBM Watson)
                    wer_1 = wer(reference, hypothesis_1)
                    cer_1 = cer(reference, hypothesis_1)
                    mer_1 = mer(reference, hypothesis_1)
                    wil_1 = wil(reference, hypothesis_1)

                    # Calculate the error rates for the second hypothesis (WhisperX)
                    wer_2 = wer(reference, hypothesis_2)
                    cer_2 = cer(reference, hypothesis_2)
                    mer_2 = mer(reference, hypothesis_2)
                    wil_2 = wil(reference, hypothesis_2)

                    # Write the results for both ASR systems to the CSV file
                    writer.writerow({
                        'FileName': ref_file,
                        'WER_IBM_Watson': f"{wer_1:.2%}",
                        'WER_WhisperX': f"{wer_2:.2%}",
                        'CER_IBM_Watson': f"{cer_1:.2%}",
                        'CER_WhisperX': f"{cer_2:.2%}",
                        'MER_IBM_Watson': f"{mer_1:.2%}",
                        'MER_WhisperX': f"{mer_2:.2%}",
                        'WIL_IBM_Watson': f"{wil_1:.2%}",
                        'WIL_WhisperX': f"{wil_2:.2%}"
                    })

                    print(f"Processed: {ref_file}")
                else:
                    print(f"Missing hypothesis files for {ref_file}")


# Usage
# Updated reference path
reference_folder = "C:/Users/Rafia/Desktop/Thesis Files/ref_txt/n-ref"
# IBM Watson folder
hypothesis_folder_1 = "C:/Users/Rafia/Desktop/Thesis Files/hypo_txt/IBM Watson/n-ibm"
# WhisperX folder
hypothesis_folder_2 = "C:/Users/Rafia/Desktop/Thesis Files/hypo_txt/whisperX/n-w"
output_csv = "C:/Users/Rafia/Desktop/Thesis Files/n-results_comparison.csv"

process_folder(reference_folder, hypothesis_folder_1,
               hypothesis_folder_2, output_csv)
