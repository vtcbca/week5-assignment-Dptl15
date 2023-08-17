def replace_vowels_with_position(string):
  """
  This function replaces all vowels in a string with their position numbers.

  Args:
    string: The string to be replaced.

  Returns:
    The string with vowels replaced with their position numbers.
  """

  vowels = "aeiouAEIOU"
  new_string = ""
  for character in string:
    if character in vowels:
      position = vowels.find(character) + 1
      new_string += str(position)
    else:
      new_string += character
  return new_string


def main():
  """
  This function prompts the user to enter a string and prints the string with vowels replaced with their position numbers.
  """

  string = input("Enter a string: ")
  new_string = replace_vowels_with_position(string)
  print(f"The string with vowels replaced with their position numbers is: {new_string}")


if __name__ == "__main__":
  main()
