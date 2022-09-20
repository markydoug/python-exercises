###################################################################
####################### Function Exercises ########################
###################################################################

# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(n):
    '''accepts one input and returns True if the passed input is either the number or the string 2, False otherwise.
    '''
    return n in (2, '2')

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(n):
  return n.lower() in ("a", "e", "i", "o", "u")

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(n):
  return n.lower() not in ("a", "e", "i", "o", "u")

# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def capitalize_if_consonant(n):
  word = ""
  if n[0].lower() not in ("a", "e", "i", "o", "u"):
    word = n.capitalize()
  else:
    word = n
  return word

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(tip_percent, bill_total):
  return round(tip_percent * bill_total, 2)

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(original_price, discount_percentage):
  return round(original_price - (original_price*discount_percentage), 2)

# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(string_number):
  return int(string_number.replace(',', ''))

# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(num_grade):
  letter_grade = ""
  if num_grade < 60:
    letter_grade = "F"
  elif num_grade < 67:
    letter_grade = "D"
  elif num_grade < 80:
    letter_grade = "C"
  elif num_grade < 88:
    letter_grade = "B"
  else:
    letter_grade = "A"

  return letter_grade

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(words):
  for i in ("aeiouAEIOU"):
    words = words.replace(i,"")
  return words


# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
#  anything that is not a valid python identifier should be removed
#  leading and trailing whitespace should be removed
#  everything should be lowercase
#  spaces should be replaced with underscores
#   for example:
#    Name will become name
#    First Name will become first_name
#    % Completed will become completed
def normalize_name(word):
  word = word.lower()
  word = word.strip()
  word = word.replace(" ", "_")
  return word

# 11. Write a function named cumulative_sum that accepts a list of numbers 
# and returns a list that is the cumulative sum of the numbers in the list.
#cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
def cumulative_sum(my_list):
  new_list =[]
  x = 0

  for i in my_list:
    x = x + i
    new_list.append(x)
  
  return new_list