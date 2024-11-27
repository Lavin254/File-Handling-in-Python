# File Read & Write Challenge
try:
    # Open the original file for reading
    with open("input.txt", "r") as infile:
        content = infile.read()

    # Modify the content (e.g., convert to uppercase)
    modified_content = content.upper()

    # Write the modified content to a new file
    with open("output.txt", "w") as outfile:
        outfile.write(modified_content)

    print("File read and modified successfully! Check 'output.txt'.")
except FileNotFoundError:
    print("Error: 'input.txt' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
