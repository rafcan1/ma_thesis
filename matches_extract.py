import re
import csv
import html

# Load the HTML file
with open('difference.html', 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

# Extract insertions (green) and deletions (red)
insertions = re.findall(
    r'<span class="diff_add">(.*?)</span>', html_content, re.DOTALL)
deletions = re.findall(
    r'<span class="diff_sub">(.*?)</span>', html_content, re.DOTALL)

# Clean up the extracted text


def clean_text(text):
    # Decode HTML entities and replace multiple spaces with a single space
    # Converts &nbsp;, &amp;, etc. into normal characters
    text = html.unescape(text)
    text = re.sub(r'\s+', ' ', text.strip())  # Remove excess whitespace
    return text


insertions = [clean_text(item) for item in insertions]
deletions = [clean_text(item) for item in deletions]

# Split the cleaned text into words
insertions_words = [
    word for sentence in insertions for word in sentence.split()]
deletions_words = [word for sentence in deletions for word in sentence.split()]

# Create a CSV file
with open('differences.csv', 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write the header
    writer.writerow(['Insertions', 'Deletions'])

    # Write rows
    max_length = max(len(insertions_words), len(deletions_words))
    for i in range(max_length):
        insertion = insertions_words[i] if i < len(insertions_words) else ''
        deletion = deletions_words[i] if i < len(deletions_words) else ''
        writer.writerow([insertion, deletion])

print("Each word in insertions and deletions has been exported to 'differences.csv'.")
