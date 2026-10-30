"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Two numbers provided by the user via standard input.
# 2. Process: The program converts the raw text inputs into numbers (using float to support decimals), then computes the four basic arithmetic operations: addition, subtraction, multiplication, and division.
# 3. Out: The formatted results of all four operations displayed on the screen.
# 4. What happens when the second number is zero, and why: 
#    Decision: The program checks if the second number is zero before performing division and displays a friendly error/warning message instead of crashing. 
#    Why: Crashing with an unhandled exception provides a poor user experience. Handling it gracefully keeps the program running and gives clear feedback to the user.

# CHECK IT YOURSELF NOTE:
# If your program shows 3 for 7 divided by 2, it is because integer division (//) was used, or the inputs were cast as integers (int()) rather than floats (float()), which truncates any decimal remainder. In Python 3, standard division (/) with floats correctly evaluates to 3.5.

# Your code below
try:
    # Prompt the user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform the four operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    # Display results
    print(f"\n--- Results for {num1} and {num2} ---")
    print(f"Addition (+)      : {addition}")
    print(f"Subtraction (-)   : {subtraction}")
    print(f"Multiplication (*): {multiplication}")

    # Handle division by zero decision
    if num2 == 0:
        print("Division (/)      : Undefined (cannot divide by zero)")
    else:
        division = num1 / num2
        print(f"Division (/)      : {division}")

except ValueError:
    print("\nError: Please enter valid numeric values.")
