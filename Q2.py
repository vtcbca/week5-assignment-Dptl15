def digit_sum(number):
    # Convert the number to a string
    number_str = str(number)
    
    # Initialize the sum variable
    sum_of_digits = 0
    
    # Iterate through each character (digit) in the number string
    for digit in number_str:
        # Convert the digit back to an integer and add it to the sum
        sum_of_digits += int(digit)
    
    return sum_of_digits

# Get the input number from the user
number = int(input("Enter a number: "))

# Calculate the sum of its digits
sum_of_digits = digit_sum(number)

# Print the result
print("Sum of digits:", sum_of_digits)
