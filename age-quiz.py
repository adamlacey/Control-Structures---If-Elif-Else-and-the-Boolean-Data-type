# Asking user to input ages.
# Once user inputs age and is equal to or greater than 40 or below 99. Statement is printed.
# All string inputs below casted to integers.

age_str = int(input("What is your age?: ")) 
if age_str >= 40 and age_str < 99:
    age_int = int(age_str)
    print("You're over the hill!")
    
# If user enters age above 100, statement below is printed.
 
elif age_str >= 100:
    print("Sorry, you're dead.")
    
# If user enters age below 13, statement below is printed.    

elif age_str < 13:
    print("You qualify for the kiddie discount.")
    
# If user enters exact age of 21, statement below is printed.
    
elif age_str == 21:
    print("Congrats on your 21st!")
    
# If any age outwith the specific ages mentioned in the program, for example:
# If a user enters the age 14, statement below is printed.
    
else:
    print("Age is just a number.")