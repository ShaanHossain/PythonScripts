import json
import csv

def convert_json_to_csv(json_file, csv_file):
    # Open the JSON file and load the data
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Extract the headers from the first JSON object
    headers = list(data[0].keys())

    # Open the CSV file in write mode
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)

        # Write the headers to the CSV file
        writer.writerow(headers)

        # Write the JSON data to the CSV file
        for item in data:
            writer.writerow(list(item.values()))

    print(f"Conversion completed. CSV file '{csv_file}' created.")

# Specify the input JSON file path and the output CSV file path
json_file = 'input.json'
csv_file = 'output.csv'

# Call the conversion function
convert_json_to_csv(json_file, csv_file)
