import csv
import re

# Define the input and output file paths
input_file_path = '/Users/omshivaprakash/Downloads/INPUT.txt'
output_file_path = '/Users/omshivaprakash/Downloads/OUTPUT.csv'

# Define the headers for the CSV file
headers = ['relation', 'title', 'creator', 'subject', 'description', 'publisher', 'date', 'type', 'format', 'language', 'identifier']

# Regular expressions to match the fields
patterns = {
    'relation': re.compile(r'relation:\s*(https?://[^\s]+)'),
    'title': re.compile(r'title:\s*(.*)'),
    'creator': re.compile(r'creator:\s*(.*)'),
    'subject': re.compile(r'subject:\s*(.*)'),
    'description': re.compile(r'description:\s*(.*)'),
    'publisher': re.compile(r'publisher:\s*(.*)'),
    'date': re.compile(r'date:\s*(\d{4}-\d{2})'),
    'type': re.compile(r'type:\s*(.*)'),
    'format': re.compile(r'format:\s*(.*)'),
    'language': re.compile(r'language:\s*(.*)'),
    'identifier': re.compile(r'identifier:\s*(https?://[^\s]+)')
}

# Function to extract data using regex patterns
def extract_data(line, data):
    for field, pattern in patterns.items():
        match = pattern.search(line)
        if match:
            data[field] = match.group(1).strip()

# Initialize the list to store the extracted data
data_list = []

# Read the input file and extract data
with open(input_file_path, 'r', encoding='utf-8') as file:
    data = {}
    for line in file:
        extract_data(line, data)
        if line.strip() == '':
            if data:
                data_list.append(data)
                data = {}

# Write the extracted data to a CSV file
with open(output_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()
    for data in data_list:
        writer.writerow(data)

print(f'Data has been successfully written to {output_file_path}')
