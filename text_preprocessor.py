input_file = "C:/Users/Rafia/Desktop/Thesis Files/ref_txt/C38-ref.txt"
output_file = "C:/Users/Rafia/Desktop/Thesis Files/ref_txt/edited_C38-ref.txt"

# Open the input file, process it, and write to the output file
with open(input_file, "r", encoding="utf-8") as infile:
    # Read all lines from the file
    lines = infile.readlines()

# Remove unnecessary newlines and combine lines with spaces
processed_text = " ".join(line.strip() for line in lines if line.strip())

# Write the processed text to the output file
with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.write(processed_text)

print(f"Processed text saved to {output_file}")
