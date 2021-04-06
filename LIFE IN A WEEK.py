#  Ask For the User for His Age
age = input ("What Your current Age? \n")

# this is because input only give out a string
#so we need to convert it to integer
age_as_int = int(age)

# Calculate for the Number of day of the User 
day = (90 - age_as_int) * 365 

# Calculate for the Number of Weeks of the User
weeks =  (90 - age_as_int) * 52

# Calculate for the Number of Months
month = (90 - age_as_int) * 12

# Message to give the User
# in this section we use the F-string and the Curly Bracket
# so as to save time in
message = f"Your Have {day} days, {weeks} Weeks and {month} Month left."

#this Section Will Print Out the Message
print (message)
