# part 1
try:
    with open("test_file.txt", "r") as f:
        contents = f.read()
except FileNotFoundError as e:
    print(f"File not found. {e}")

# part 2

# Step 1: Create the input file (sample_input_dict.txt)
input_dict = {
    "apple": "red",
    "banana": "yellow",
    "cherry": "red",
    "mango": "yellow",
    "grapes": "black",
}

with open("sample_input_dict.txt", "w") as input_file:
    for key, value in input_dict.items():
        input_file.write(f"{key}: {value}\n")

# Step 2: Read from the input file, invert the dictionary, and write to the output file (sample_output_dict.txt)

# Function to read from the input file and invert the dictionary


def invert_dict(input_file, output_file):
    inverted_dict = {}
    with open(input_file, "r") as input_file:
        for line in input_file:
            key, value = line.strip().split(": ")
            if value not in inverted_dict:
                inverted_dict[value] = [key]
            else:
                inverted_dict[value].append(key)

    # Write the inverted dictionary to the output file
    with open(output_file, "w") as output_file:
        output_file.write("{\n")
        for key, value in inverted_dict.items():
            output_file.write(f"\n{key}: {', '.join(value)}\n")
        output_file.write("}\n")


# Perform the inversion and write to the output file
invert_dict("sample_input_dict.txt", "sample_output_dict.txt")

# Step 3: Read from the output file and print the contents to the console
with open("sample_output_dict.txt", "r") as output_file:
    for line in output_file:
        print(line.strip())


# Explanation: The code above first creates a dictionary and writes it to a file. Then, the code reads from the file, inverts the dictionary, and writes the inverted dictionary to a new file. Finally, the code reads from the new file and prints the contents to the console (i.e., the terminal).
