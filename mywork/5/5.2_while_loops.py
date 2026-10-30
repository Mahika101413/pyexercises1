"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: User input strings captured via the input() function.
# 2. Process: The program strips leading/trailing whitespace and converts the input to lowercase 
#    to normalize answers like " Yes ", "YES", and "yes". It increments an attempt counter and 
#    checks if the maximum attempt limit has been reached.
# 3. Out: Interactive prompt messages asking for input, feedback loops, and a final summary 
#    detailing whether the goal was met or the limit was hit.
# 4. My stop condition, my attempt limit, my summary: 
#    - Stop condition: The user inputs "yes" (case-insensitive and ignoring extra spaces).
#    - Attempt limit: Maximum of 3 attempts. If reached without success, the program terminates safely.
#    - Summary: Displays whether the user succeeded or failed, the total number of attempts used, 
#      and the final input received.

# Your code below
max_attempts = 3
attempts = 0
success = False
user_input = ""

print("--- Confirmation Required ---")

while attempts < max_attempts and not success:
    # Ask the user for input
    user_input = input(f"Attempt {attempts + 1} of {max_attempts} — Do you agree to proceed? (Type 'yes'): ")
    attempts += 1
    
    # Normalize input by stripping whitespace and converting to lowercase 
    # (this handles "Yes", "yes", " yes ", and "YES")
    cleaned_input = user_input.strip().lower()
    
    if cleaned_input == "yes":
        success = True
    else:
        if attempts < max_attempts:
            print("Incorrect answer. Please try again.\n")

print("\n=== LOOP SUMMARY ===")
if success:
    print(f"Status: SUCCESS")
    print(f"Total attempts made: {attempts}")
    print(f"Your final response ('{user_input}') was accepted.")
else:
    print(f"Status: FAILED / LOCKED OUT")
    print(f"Maximum safety limit of {max_attempts} attempts reached.")
    print("Action cancelled due to repeated invalid inputs.")