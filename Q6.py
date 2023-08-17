def print_substring(string, start_char, end_char):
    # Find the indices of the start and end characters
    start_index = string.index(start_char)
    end_index = string.index(end_char)

    # Extract the substring based on the indices
    substring = string[start_index:end_index+1]

    return substring

# Get the input string from the user
string = input("Enter a string: ")

# Get the start character from the user
start_char = input("Enter the start character: ")

# Get the end character from the user
end_char = input("Enter the end character: ")

# Print the substring
substring = print_substring(string, start_char, end_char)
print("Substring:", substring)
