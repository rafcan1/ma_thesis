import pandas as pd
import editdistance
from jiwer import compute_measures

# Function to read text files


def read_from_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        text = ''.join(lines)
        return text

# Function to process and analyze alignment for a single file


def process_file(reference_file, hypothesis_file):
    # Read reference and hypothesis
    reference_text = read_from_file(reference_file)
    hypothesis_text = read_from_file(hypothesis_file)

    # Compute alignment and measures using jiwer
    measures = compute_measures(reference_text, hypothesis_text)

    # Print overall WER
    print(f"Word Error Rate (WER): {measures['wer']:.2%}")
    print(f"Insertions: {measures['insertions']}")
    print(f"Deletions: {measures['deletions']}")
    print(f"Substitutions: {measures['substitutions']}")

    # Perform detailed alignment using editdistance
    ref_words = reference_text.split()
    hyp_words = hypothesis_text.split()

    # Get the edit distance transformation matrix
    dist_matrix = editdistance.eval(ref_words, hyp_words)

    # Prepare a list to store error details
    error_details = []

    # Collect errors (substitutions, deletions, insertions)
    for i, ref_word in enumerate(ref_words):
        if i < len(hyp_words):
            if ref_word != hyp_words[i]:
                error_details.append({
                    'Error Type': 'Substitution',
                    'Reference': ref_word,
                    'Hypothesis': hyp_words[i]
                })
        else:
            error_details.append({
                'Error Type': 'Deletion',
                'Reference': ref_word,
                'Hypothesis': ''
            })

    # Add insertions (if any words in hypothesis are extra)
    for i in range(len(ref_words), len(hyp_words)):
        error_details.append({
            'Error Type': 'Insertion',
            'Reference': '',
            'Hypothesis': hyp_words[i]
        })

    # Return the error details along with the computed measures
    return error_details, measures

# Function to display results in a table format


def display_results_in_table(error_details, measures):
    # Create a pandas DataFrame for error details
    df = pd.DataFrame(error_details)

    # Display the error details table
    print("\nError Details:")
    print(df)

    # Display the overall measures in a separate table
    measures_table = pd.DataFrame([{
        'WER': measures['wer'],
        'Insertions': measures['insertions'],
        'Deletions': measures['deletions'],
        'Substitutions': measures['substitutions']
    }])
    print("\nOverall Measures:")
    print(measures_table)


# File paths
hypothesis = read_from_file(
    "C:/Users/Rafia/Desktop/ASR/hypo_txt/IBM Watson/C22-hypo-ibm.txt")
reference = read_from_file(
    "C:/Users/Rafia/Desktop/ASR/ref_txt/edited_C22-ref.txt")

# Process the file
error_details, measures = process_file(reference, hypothesis)

# Display the results in a table format
display_results_in_table(error_details, measures)
