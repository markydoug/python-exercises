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

#Calculate cost
total_cost = (brother_bear+hercules+little_mermaid)*movie_price

#Print cost
print("You will have to pay $" + str(total_cost))


##Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

#Define salary per hour
google_per_hour = 400
amazon_per_hour = 380
facebook_per_hour = 350

#Define this week's hours
facebook_hours = 10
google_hours = 6
amazon_hours = 4

#Calculate salary
this_week_paycheck = (facebook_per_hour * facebook_hours) + (google_per_hour * google_hours) + (amazon_per_hour * amazon_hours)

#Print out salary
print("You should receive $" + str(this_week_paycheck))

##A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.


##A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.
