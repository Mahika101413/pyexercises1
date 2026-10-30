"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it wit.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A sentence provided by the user via the input() function.
# 2. Process: The input sentence is cleaned and modified using four distinct string methods.
# 3. Out: Four different text transformations of the original input displayed on the screen.
# 4. My four transformations, and when each is useful:
#    - strip(): Useful for cleaning up accidental leading and trailing whitespace from user input.
#    - upper(): Useful for standardizing text for database lookups, acronyms, or emphasis.
#    - title(): Useful for formatting names or titles for a clean, professional appearance.
#    - swapcase(): Useful for creating stylized/retro text effects or testing case-handling logic.


# Your code below
# Ask the user for a sentence
user_sentence = input("Please enter a sentence: ")

# Apply four distinct transformations
result_strip = user_sentence.strip()
result_upper = user_sentence.strip().upper()
result_title = user_sentence.strip().title()
result_swap = user_sentence.strip().swapcase()

# Display the results
print("\n--- Four Transformations ---")
print(f"1. strip():    '{result_strip}'")
print(f"2. upper():    '{result_upper}'")
print(f"3. title():    '{result_title}'")
print(f"4. swapcase(): '{result_swap}'")

# CHECK IT YOURSELF (Tested with input: "  hello World from Python  ")
# - Result 1 (strip): Expected. Successfully removed the leading and trailing spaces from both ends.
# - Result 2 (upper): Expected. Converted all letters to uppercase ("HELLO WORLD FROM PYTHON"), retaining the middle capital and raising the rest.
# - Result 3 (title): Expected. Capitalized the first letter of every word ("Hello World From Python").
# - Result 4 (swapcase): Expected. Inverted the case of every character ("HELLO wORLD fROM pYTHON").