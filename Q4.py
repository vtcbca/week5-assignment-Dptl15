def is_armstrong(number):
  """
  This function checks if a number is Armstrong number.

  Args:
    number: The number to be checked.

  Returns:
    True if the number is Armstrong number, False otherwise.
  """

  sum_of_powers = 0
  original_number = number
  digits = len(str(number))
  while number > 0:
    digit = number % 10
    sum_of_powers += digit ** digits
    number //= 10

  return original_number == sum_of_powers


def main():
  """
  This function prompts the user to enter a number and prints whether the number is Armstrong number or not.
  """

  number = int(input("Enter a number: "))
  if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
  else:
    print(f"{number} is not an Armstrong number.")


if __name__ == "__main__":
  main()
