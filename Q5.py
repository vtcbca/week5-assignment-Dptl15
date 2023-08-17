def count_vowels(string):
    # Convert the string to lowercase for case-insensitive matching
    string = string.lower()
    
    # Define a set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Initialize the vowel count
    vowel_count = 0
    
    # Iterate through each character in the string
    for char in string:
        # Check if the character is a vowel
        if char in vowels:
            vowel_count += 1
    
    return vowel_count

# Get the input string from the user
string = input("Enter a string: ")

# Count the number of vowels
vowel_count = count_vowels(string)

# Print the result
print("Number of vowels:", vowel_count)
