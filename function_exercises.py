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
  # check to see if the first letter is not a vowel. in other words a consonant
  if n[0].lower() not in ("a", "e", "i", "o", "u"):
    # capitalize the first letter of the words and stores in the variable word as a string
    print(n.capitalize())
  else:
    #if not a consonant just print out the original word
    print(n)

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(tip_percent, bill_total):
  #take in the tip percentage and multiply it by the total bill and round to two decimals and return the value
  return round(tip_percent * bill_total, 2)

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(original_price, discount_percentage):
    #multiply the original price and the discount percentage and subtract that fom the original price, return that
  return round(original_price - (original_price*discount_percentage), 2)

# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(string_number):
    #take the string passed and take out the commas and return an int
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
   #check to see if each letter of the word is a vowel 
  for i in ("aeiouAEIOU"):
    #for each vowel that is in the string, we replace it with nothing
    words = words.replace(i,"")
  #return the new word without vowels
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
     #check if there are any special characters
    for ch in ['*','{','}','[',']','(',')','>','#','+','-','.','!','$','\'','@','%']:
        #if there is a special character
        if ch in word:
            #replace the special character with nothing
            word = word.replace(ch,"") 
    #take out any leading or tailing space
    word = word.strip()
    #replace any spaces with _
    word = word.replace(" ", "_")
    #make the word all lowercase
    word = word.lower()
    #return the string as a valid identifier
    return word

# 11. Write a function named cumulative_sum that accepts a list of numbers 
# and returns a list that is the cumulative sum of the numbers in the list.
#cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
def cumulative_sum(my_list):
  #create an empty list
  new_list =[]
  #define x so that we can multiply by it in the for loop
  x = 0

  #take every number in the list
  for i in my_list:
    #take the number from the list and add it to x
    x += i
    #add the new x to your list
    new_list.append(x)
  #return the list of new numbers
  return new_list


  ######################BONUS########################

# 1. Create a function named twelveto24. It should accept a string in the format 10:45am 
# or 4:30pm and return a string that is the representation of the time in a 24-hour format. 


# Bonus write a function that does the opposite.


# 2.Create a function named col_index. It should accept a spreadsheet column name, and return 
# the index number of the column.