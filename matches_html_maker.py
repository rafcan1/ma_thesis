import difflib

# Read the files
with open("C:/Users/Rafia/Desktop/ASR/ref_txt/edited_C22-ref.txt", encoding='utf-8') as file1:
    first_file_content = file1.read()

with open("C:/Users/Rafia/Desktop/ASR/hypo_txt/IBM Watson/C22-hypo-ibm.txt", encoding='utf-8') as file2:
    second_file_content = file2.read()

# Split the content into words
first_file_lines = first_file_content.split()
second_file_lines = second_file_content.split()

# Generate the HTML difference
difference = difflib.HtmlDiff().make_file(
    first_file_lines,
    second_file_lines,
    'first_file',
    'second_file'
)

# Write the difference to an HTML file
with open('differences.html', 'w', encoding='utf-8') as difference_report:
    difference_report.write(difference)
