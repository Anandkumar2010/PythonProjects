"""
PROJECT: Voting Eligibility Checker
Goal: Practice Python input handling, error handling, and conditional logic
Author: Anand Kumar Yadav
"""

while True:
    print("\n--- Voting Verification System ---")

    # 1. Name Input
    name = input("Enter Your Name: ")

    # 2. Age Verification
    try:
        age = int(input("Enter Your Age: "))
        if age < 0:
            print("Invalid Age - RESTARTING...")
            continue
        elif age < 18:
            print("Error: You are not old enough to vote. RESTARTING...")
            continue
    except ValueError:
        print("Oops! You must enter a number for Age, RESTARTING...")
        continue

    # 3. Mobile Verification (Now correctly inside the loop)
    mob_no = input("Enter Your Mobile No: ")
    if not mob_no.isdigit():
        print("Oops! You must enter a number for Mobile No. RESTARTING...")
        continue

    print(f"OTP was sent to: {mob_no}")

    # 4. OTP Verification
    OTP = input("Enter your OTP: ")
    if OTP != "1234":
        print("Error: Incorrect OTP. Restarting...")
        continue

    print("Mobile Number was successfully verified")

    # 5. Email Verification
    email = input("Enter Your Email Address: ")
    if "@" not in email:
        print("Error: Invalid email format. Restarting...")
        continue

    print(f"A code was sent to {email}, please enter it below")

    # Simple code check
    try:
        email_code = int(input("Enter your Code: "))
        print("Email verified successfully")
    except ValueError:
        print("Error: Code must be a number. Restarting...")
        continue

    # 6. Party Selection
    print("\nSelect the party you want to vote for:")
    print("1. Party A")
    print("2. Party B")
    print("3. Party C")

    choice = input("Enter 1, 2, or 3: ")

    if choice in ["1", "2", "3"]:
        print(f"Thank you, {name}! Your vote for Party {choice} has been cast.")
        break  # Exits the loop, ending the program
    else:
        print("Error: Invalid choice. Restarting...")
        continue
