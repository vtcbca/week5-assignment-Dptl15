def is_palindrome(number):
  """
  This function checks if a number is palindrome.

  Args:
    number: The number to be checked.

  Returns:
    True if the number is palindrome, False otherwise.
  """

  reversed_number = 0
  original_number = number
  while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

  return original_number == reversed_number


def main():
  """
  This function prompts the user to enter a number and prints whether the number is palindrome or not.
  """

  number = int(input("Enter a number: "))
  if is_palindrome(number):
    print(f"{number} is a palindrome.")
  else:
    print(f"{number} is not a palindrome.")


if __name__ == "__main__":
  main()
