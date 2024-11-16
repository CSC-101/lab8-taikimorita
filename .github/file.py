import sys

def process_file(filename: str) -> None:
    """
    Purpose
    - This function reads a file line by line and processes each line to calculate and print the sum of two float values found in each line.
    - If a line does not contain exactly two values or if the values cannot be converted to floats, an error message is displayed for that line.

    Input
    - A string representing the filename to be opened and read.

    Output
    - None. Prints the sum of the two float values for each valid line or an error message for invalid lines.

    Data Representation
    - The input is expected to be a text file where each line contains exactly two values separated by whitespace.
    - The function processes each line by splitting the values and attempting to convert them to floats.
    """
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    values = line.split()
                    if len(values) != 2:
                        raise ValueError("Line does not contain exactly two values")
                    num1, num2, = float(values[0]), float(values[1])
                    print(f"Sum of line {line_number}: {num1 + num2}")
                except ValueError as e:
                    print(f"Error in line {line_number}: {e}")
    except FileNotFoundError:
        print("Error: File not found or could not be opened")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python file.py <filename>")
        sys.exit(1)
    process_file(sys.argv[1])
