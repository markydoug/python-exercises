#Identify the data type of the following values:

type(99.9) # float

type("False") #str

type(False) #bool

type('0') #str

type(0) #int

type(True) #bool

type('True') #str

type([{}]) #list

type({'a': []}) #dict

#What data type would best represent:

#A term or phrase typed into a search box? str

#If a user is logged in? bool

#A discount amount to apply to a user's shopping cart? int

#Whether or not a coupon code is valid? bool

#An email address typed into a registration form? str

#The price of a product? float

#A Matrix? dict

#The email addresses collected from a registration form? list

#Information about applicants to Codeup's data science program? dict


#########################################################################
#For each of the following code blocks, read the expression and predict what 
#the result of evaluating it would be, then execute the expression in your Python REPL.

'1' + 2 
#Prediction: error
#Actual: error

6 % 4
#Prediction: 2
#Actual: 2

type(6 % 4)
#Prediction: int
#Actual: int

type(type(6 % 4))
#Prediction: int
#Actual: type

'3 + 4 is ' + 3 + 4
#Prediction: Error
#Actual: Error

0 < 0
#Prediction: False
#Actual: False

'False' == False
#Prediction: False
#Actual: False

True == 'True'
#Prediction: False
#Actual: False

5 >= -5
#Prediction: True
#Actual: True

True or "42"
#Prediction: error
#Actual: True

6 % 5
#Prediction: 1
#Actual: 1

5 < 4 and 1 == 1
#Prediction: False
#Actual: False

'codeup' == 'codeup' and 'codeup' == 'Codeup'
#Prediction: False
#Actual: False

4 >= 0 and 1 != '1'
#Prediction: True
#Actual: False

6 % 3 == 0
#Prediction: True
#Actual: True

5 % 2 != 0
#Prediction: True
#Actual: True

[1] + 2
#Prediction: [3]
#Actual: error

[1] + [2]
#Prediction: [1,2]
#Actual: [1,2]

[1] * 2
#Prediction: error
#Actual: [1, 1]

[1] * [2]
#Prediction: [2, 2]
#Actual: error

[] + [] == []
#Prediction: True
#Actual: True

{} + {}
#Prediction: error
#Actual: error



######################################################
## Write some Python code, that is, variables and operators, 
## to describe the following scenarios. Do not worry about the 
## real operations to get the values, the goal of these exercises 
## is to understand how real world conditions can be represented with code.

##You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?
#Define movie price
movie_price = 3

#Define rental length
brother_bear = 5
hercules = 1
little_mermaid = 3
movie_rental_days = [brother_bear, hercules, little_mermaid]

#Calculate cost
total_cost_per_movie = [days * movie_price for days in movie_rental_days]
total_cost = sum(total_cost_per_movie)

#Print cost
print("You need to pay $" + str(total_cost))


##Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
#Define salary per hour
google_per_hour = 400
amazon_per_hour = 380
facebook_per_hour = 350
salary_per_hour = [google_per_hour, amazon_per_hour, facebook_per_hour]

#Define this week's hours
facebook_hours = 10
google_hours = 6
amazon_hours = 4
hours_worked = [facebook_hours, google_hours, amazon_hours]

#Calculate salary
this_week_paycheck = [item1 * item2 for item1, item2 in zip(salary_per_hour, hours_worked)]

#Print out salary
print("You should receive $" + str(sum(this_week_paycheck)))


##A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.
#Define class data
max_students = 25
class_time = '10:00'

#Define specific variables to determine if student can enroll
students_enrolled = 20
student_schedule = ['10:00', '12:00', '15:00']

#Check if class is full
class_not_full = students_enrolled < max_students

#Check if the student's schedule has a conflict
if class_time in student_schedule:
  class_no_conflict = False
else: 
  class_no_conflict = True
    
#Tell us if she can enroll
can_enroll = class_not_full == True and class_no_conflict == True
if can_enroll == True:
    print('She can enroll!')
else:
    print('She cannot join this class.')
    
##A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

#Customer info
premium_member = True
purchased_items = 1
purchase_date = '2022-09-16'

#Offer info
offer_expire_date = '2022-09-20'

#Check if offer available
if (purchased_items > 2 or premium_member == True) and purchase_date < offer_expire_date:
    offer_available = True
else: offer_available = False

#Tell the customer the results
if offer_available == True:
    print('You have a product offer available!')
else:
    print('Thank you for shopping with us.')

########################################################

username = 'codeup'
password = 'notastrongpassword'

##Create a variable that holds a boolean value for each of the following conditions:

#the password must be at least 5 characters
len(password) >= 5

#the username must be no more than 20 characters
len(username) <= 20

#the password must not be the same as the username
username != password

#bonus neither the username or password can start or end with whitespace
(username.isspace() == False) and (password.isspace() == False)