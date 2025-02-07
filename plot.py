import matplotlib.pyplot as plt
import editdistance
from jiwer import compute_measures

# Example reference and hypothesis texts


def read_from_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        text = ''.join(lines)
        return text


hypothesis = read_from_file(
    "C:/Users/Rafia/Desktop/ASR/hypo_txt/whisperX/e-C22-hypo-w.txt")
reference = read_from_file(
    "C:/Users/Rafia/Desktop/ASR/ref_txt/edited_C22-ref.txt")
# Compute alignment and measures
measures = compute_measures(reference, hypothesis)

# Print overall WER
print(f"Word Error Rate (WER): {measures['wer']:.2%}")

# Print detailed error types
print(f"Insertions: {measures['insertions']}")
print(f"Deletions: {measures['deletions']}")
print(f"Substitutions: {measures['substitutions']}")

# Perform detailed alignment using editdistance
ref_words = reference.split()
hyp_words = hypothesis.split()

# Get the edit distance transformation matrix
dist_matrix = editdistance.eval(ref_words, hyp_words)

# Print detailed transformations
for i, ref_word in enumerate(ref_words):
    if i < len(hyp_words):
        if ref_word != hyp_words[i]:
            print(f"Error Type: Substitution")
            print(f"Reference: '{ref_word}'")
            print(f"Hypothesis: '{hyp_words[i]}'")
    else:
        print(f"Error Type: Deletion")
        print(f"Reference: '{ref_word}'")
    print("-" * 50)  # Separator for readability

# Count the types of errors (substitutions, deletions, insertions)
error_types = {'substitute': measures['substitutions'],
               'delete': measures['deletions'],
               'insert': measures['insertions']}


def plot_error_types(error_counts):
    # Determine the maximum count across all error types
    max_count = max(error_counts.values())
    # Plot the error types
    plt.bar(error_types.keys(), error_types.values(),
            color=['red', 'blue', 'green'])
    plt.title("Error Types Breakdown")
    plt.ylabel("Count")
    plt.xlabel("Error Type")
    plt.ylim(0, max_count + 1)
    plt.show()

    plot_error_types(error_counts)
