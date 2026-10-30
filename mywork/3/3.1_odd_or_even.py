"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: An integer N entered by the user via the console.
# 2. Process: The program validates the input, checks if N > 0, and loops from 1 to N. Inside the loop, the modulo operator (% 2) checks whether each number is divisible by 2 to determine if it is odd or even.
# 3. Out: Text printed to the console stating whether each number from 1 to N is "odd" or "even".
# 4. What happens on 0, on a negative number, on a very large number:
#    - 0 or a negative number: The program prints a clear error message stating that N must be a positive integer greater than 0 and stops without looping.
#    - 5000 (very large number): The program proceeds and prints all 5000 lines (which Python executes instantly), though we include a small check to notify the user.

# CHECK IT YOURSELF RESULTS:
# - Run with 6: Successfully printed 3 odd numbers (1, 3, 5) and 3 even numbers (2, 4, 6). Counted and verified.
# - Run with 0: Correctly caught the edge case, printed the error message, and stopped.
# - Run with -4: Correctly caught the negative number, printed the error message, and stopped.
# - Run with 5000: Displayed the large-number notice and successfully printed all 5000 lines.

# Your code below
try:
    user_input = input("Enter a positive integer N: ")
    N = int(user_input)
except ValueError:
    print("Invalid input. Please enter a valid whole number.")

# Handle 0 or negative numbers
if N <= 0:
    print(f"Error: N must be greater than 0. You entered {N}.")


# Handle very large numbers (like 5000)
if N >= 5000:
    print(f"Notice: {N} is a large number. Printing all results...")

# Loop from 1 to N
for i in range(1, N + 1):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")