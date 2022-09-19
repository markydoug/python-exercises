## 1.Conditional Basics
#a. prompt the user for a day of the week, print out whether the day is Monday or not
day = input("What day?")
if day.lower() == 'monday':
  print("It's Monday!")
else:
  print("It's  not Monday.")

#b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
day = input("What day?")
if day.lower() in ('saturday', 'sunday'):
  print("It's the weekend!")
else:
  print("It's not the weekend.")

#c. create variables and make up values for
#the number of hours worked in one week
hours_worked_in_one_week = 24

#the hourly rate
hourly_rate = 8.75

#how much the week's paycheck will be
paycheck_this_week = hours_worked_in_one_week * hourly_rate

#write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
if hours_worked_in_one_week > 40:
    paycheck_this_week = hours_worked_in_one_week * hourly_rate * 1.5
else:
    paycheck_this_week = hours_worked_in_one_week * hourly_rate
print("Your paycheck should be: $" + str(round(paycheck_this_week,2)))

## 2.Loop Basics
#While
#Create an integer variable i with a value of 5.
i = 5

#Create a while loop that runs so long as i is less than or equal to 15
while i <= 15:
    print(i)
    i += 1

#Each loop iteration, output the current value of i, then increment i by one.
while i <= 15:
    print(i)
    i += 1

#Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
t = 0 
while t <= 100:
    print(t)
    t += 2

#Alter your loop to count backwards by 5's from 100 to -10.
n = 100 
while n >= -10:
    print(n)
    n -= 5

#Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. 
a = 2 
while a < 1000000:
    print(a)
    a = a**2

#Write a loop that uses print to create the output shown below.
n = 100 
while n >= 5:
    print(n)
    n -= 5

#For Loops
#Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
n = int(input("Give me a number: "))
for i in range(1,11):
  print(str(n) + " x " +str(i) + " = " + str(i*n))

#Create a for loop that uses print to create the output shown below.
for i in range(1,10):
  print(str(i)*i)

#break and continue
#Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.
pos_num = int(input("Please enter a postitive integer: "))

if pos_num <=0:
  print("Please enter a positive number!!!")
else:
  while pos_num > 0:
    pos_num -= 1

#Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)
pos_num = int(input("Please enter a postitive integer: "))

if pos_num <=0:
  print("Please enter a positive number!!!")
else:
  for n in range(pos_num+1):
    print(n)
    if n > pos_num:
      break

#Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
pos_num = int(input("Please enter a postitive integer: "))

if pos_num <=0:
  print("Please enter a positive number!!!")
else:
  while pos_num > 0:
    print(pos_num)
    pos_num -= 1

## 3.Fizzbuzz
#Write a program that prints the numbers from 1 to 100.

#For multiples of three print "Fizz" instead of the number

#For the multiples of five print "Buzz".

#For numbers which are multiples of both three and five print "FizzBuzz".


## 4.Display a table of powers.
#Prompt the user to enter an integer.

#Display a table of squares and cubes from 1 to the value entered.

#Ask if the user wants to continue.

#Assume that the user will enter valid data.

#Only continue if the user agrees to.

#Bonus: Research python's format string specifiers to align the table


##5. Convert given number grades into letter grades.

#Prompt the user for a numerical grade from 0 to 100.

#Display the corresponding letter grade.

#Prompt the user to continue.

#Assume that the user will enter valid integers for the grades.

#The application should only continue if the user agrees to.

#Bonus: Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

## 6.Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.

#Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.