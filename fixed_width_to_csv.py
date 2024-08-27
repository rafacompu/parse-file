import csv


# Function to parse the spec file, which defines the width of each field
def parse_spec_file(spec_file):
    with open(spec_file, 'r', encoding='utf-8') as file:
        # Read the spec file and convert each line to an integer
        # Each integer represents the width of a corresponding field
        spec = [int(line.strip()) for line in file.readlines()]
    return spec


# Function to parse the fixed-width file using the spec
def parse_fixed_width_file(fixed_width_file, spec):
    parsed_data = []
    with open(fixed_width_file, 'r', encoding='utf-8') as file:
        for line in file:
            parsed_line = []
            start = 0
            # Loop through each field width in the spec
            for width in spec:
                # Extract the substring corresponding to the current field
                # Strip any extra spaces that might have been used for padding
                parsed_line.append(line[start:start + width].strip())
                # Update the starting index for the next field
                start += width
            # Append the parsed fields as a list (representing a row) to the parsed_data
            parsed_data.append(parsed_line)
    return parsed_data


# Function to write the parsed data to a CSV file
def write_csv(output_file, data):
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        # Create a CSV writer object
        writer = csv.writer(file)
        # Write each row of data to the CSV file
        writer.writerows(data)


# Main script execution starts here
if __name__ == "__main__":
    # Parse the spec file to get the widths of each field
    spec = parse_spec_file('spec.txt')
    # Parse the fixed-width file based on the spec to extract the data
    data = parse_fixed_width_file('sample_fixed_width.txt', spec)
    # Write the parsed data to an output CSV file
    write_csv('output.csv', data)
    print("Conversion successful. Output written to 'output.csv'.")
