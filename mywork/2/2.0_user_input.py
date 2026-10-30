"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. What goes in? 
#    - The user's favorite book genre (text/string).
#    - The number of books they have read this year (number entered as text, then converted).

# 2. What happens to it? 
#    - The program captures both inputs, converts the book count string into a numeric integer so math can be performed, and combines everything into a formatted output sentence.

# 3. What comes out? 
#    - A personalized status sentence acknowledging their favorite genre and setting a stretched reading target for next year.

# 4. My two fields, and what I would do with them:
#    - Field 1: Favorite book genre. Purpose: In a future library or bookstore app, this would be used to curate tailored book recommendations and targeted discounts.
#    - Field 2: Books read this year. Purpose: To track personal reading milestones, award achievement badges, and calculate progress toward an annual reading goal.


# --- CHECK IT YOURSELF OBSERVATIONS ---
# 1. Empty line input: 
#    - input() returns an empty string (""). 
#    - Trying to convert it using int("") raises a `ValueError: invalid literal for int() with base 10: ''`.
#
# 2. Space input: 
#    - input() returns a space character (" "). 
#    - Trying to convert it using int(" ") raises a `ValueError: invalid literal for int() with base 10: ' '`.
#
# 3. Text where a number was expected (e.g., typing "five"): 
#    - input() returns the string "five". 
#    - Trying to convert it using int("five") raises a `ValueError: invalid literal for int() with base 10: 'five'`.
# ----------------------------------------


# Your code below

# Ask the user for the two fields
genre = input("What is your favorite book genre? ")
books_input = input("How many books have you read this year? ")

# Note on adding 1: 
# If you try to do `books_input + 1` directly without converting it, Python raises a 
# `TypeError: can only concatenate str (not "int") to str` because `input()` always returns a string.
# To deal with this, we convert the string to an integer using int() and use a try/except 
# block to gracefully handle the edge cases tested above.

try:
    books_read = int(books_input)
    next_goal = books_read + 1
    print(f"\nThat's awesome! As a fan of {genre}, reading {books_read} books this year is a great achievement.")
    print(f"If you read just one more, your next target is {next_goal} books!")
except ValueError:
    print(f"\nOops! You entered an invalid number for your book count. As a fan of {genre}, please enter a whole number next time.")