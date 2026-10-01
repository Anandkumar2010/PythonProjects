import sys

# Initialize the user's quiz score
score = 0

# Display the welcome message
print("Welcome to My Fun Quiz")

# Ask the user whether they want to start the quiz
play = input("Do You Want To Play? ").strip().upper()

# Continue only if the user agrees to play
if play == "YES" or play == "Y":
    print("Let's Play")
else:
    print("Thanks for Playing")
    sys.exit()

# Display a short introduction before the quiz begins
print("Before We Start, Let's have an Introduction")

# Collect basic user information
name = input("What is your name? ")
print(f"Hello {name}, Welcome to My Fun Quiz")

# Verify the user's age before continuing
age = int(input("What is your age? "))

if age >= 18:
    print("You're old enough. Let's Play!")
else:
    print("You are not old enough, buddy.")
    sys.exit()

# -------------------- Question 1 --------------------
Ques1 = input(
    "What is the capital of Australia?\n"
    "A. Sydney\n"
    "B. Melbourne\n"
    "C. Canberra\n"
    "D. Perth\n"
)

# Validate the user's answer and update the score
if Ques1.lower() == "canberra" or Ques1.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# -------------------- Question 2 --------------------
Ques2 = input(
    "Which planet is known as the Red Planet?\n"
    "A. Venus\n"
    "B. Mars\n"
    "C. Jupiter\n"
    "D. Saturn\n"
)

if Ques2.lower() == "mars" or Ques2.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# -------------------- Question 3 --------------------
Ques3 = input(
    "Who developed Python?\n"
    "A. James Gosling\n"
    "B. Dennis Ritchie\n"
    "C. Guido van Rossum\n"
    "D. Bjarne Stroustrup\n"
)

if Ques3.lower() == "guido van rossum" or Ques3.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# -------------------- Question 4 --------------------
Ques4 = input(
    "Which is the largest ocean on Earth?\n"
    "A. Atlantic Ocean\n"
    "B. Indian Ocean\n"
    "C. Arctic Ocean\n"
    "D. Pacific Ocean\n"
)

if Ques4.lower() == "pacific ocean" or Ques4.lower() == "d":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# -------------------- Question 5 --------------------
Ques5 = input(
    "What does CPU stand for?\n"
    "A. Central Program Unit\n"
    "B. Central Processing Unit\n"
    "C. Computer Power Unit\n"
    "D. Central Performance Unit\n"
)

if Ques5.lower() == "central processing unit" or Ques5.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# -------------------- Question 6 --------------------
Ques6 = input(
    "Which data type stores True or False values in Python?\n"
    "A. Integer\n"
    "B. String\n"
    "C. Float\n"
    "D. Boolean\n"
)

if Ques6.lower() == "boolean" or Ques6.lower() == "d":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# -------------------- Question 7 --------------------
Ques7 = input(
    "Which language is primarily used for styling web pages?\n"
    "A. HTML\n"
    "B. JavaScript\n"
    "C. CSS\n"
    "D. SQL\n"
)

if Ques7.lower() == "css" or Ques7.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# -------------------- Question 8 --------------------
Ques8 = input(
    "Which gas do plants absorb from the atmosphere?\n"
    "A. Oxygen\n"
    "B. Nitrogen\n"
    "C. Hydrogen\n"
    "D. Carbon Dioxide\n"
)

if Ques8.lower() == "carbon dioxide" or Ques8.lower() == "d":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# -------------------- Question 9 --------------------
Ques9 = input(
    "Which keyword is used to define a function in Python?\n"
    "A. function\n"
    "B. define\n"
    "C. def\n"
    "D. func\n"
)

if Ques9.lower() == "def" or Ques9.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# -------------------- Question 10 --------------------
Ques10 = input(
    "Which planet has the most moons (according to current discoveries)?\n"
    "A. Jupiter\n"
    "B. Earth\n"
    "C. Mars\n"
    "D. Saturn\n"
)

if Ques10.lower() == "saturn" or Ques10.lower() == "d":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Display the user's final score
print(f"\n{name}, you scored {score}/10")
