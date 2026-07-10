# Take input from the user

first_name = input("Enter Your Name")
last_name = input("Enter Your Last Name")
age = int(input("Enter Your Age"))
# Add if elif else condition with appropriate intendation
if age >= 18: # To insure only adults are able to sign up
    print("Sorry, you are not eligible to sign up")
elif age >= 18:
    print("You are eligible to sign up")
else:
    print("Please Enter a Valid Age") # To be sure that the user is giving a valid input

