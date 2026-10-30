"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - Contains blank/empty lines.
# - Inconsistent capitalization (mixed uppercase, lowercase, and title case).
# - Extra whitespace (leading spaces, trailing spaces, tabs, and multiple spaces between words).
# - Duplicate entries (several names appear multiple times).
# - Inconsistent name ordering/formatting (some are in "First Last" format while others are in "Last, First" format).

# 1. In: The raw text file `names.txt` containing unformatted, messy person names.
# 2. Process, problem by problem:
#    - Blank lines: Skipped during iteration.
#    - Inconsistent capitalization: Standardized to proper title case (preserving lowercase particles where applicable).
#    - Extra whitespace: Stripped and normalized using `.strip()` and word-splitting.
#    - Duplicate entries: Filtered out using a set to ensure uniqueness.
#    - Inconsistent formatting ("Last, First"): Converted to standard "First Last" format by splitting at the comma and rearranging.
# 3. Out: A new file named `cleaned_names.txt` containing unique, properly formatted, and sorted names.
# 4. How I decide which word is the last name: For names formatted as "Last, First", the last name is the part before the comma. For names formatted as "First Last", the last name is identified as the final word (or final components including common particles like "van"), and sorting is keyed on this extracted last name.


# Your code below
import os

INPUT_FILE = "names.txt"
OUTPUT_FILE = "cleaned_names.txt"

def clean_and_format_name(line):
    line = line.strip()
    if not line:
        return None
    
    # Handle "Last, First" format (e.g., "Chen, Wei")
    if "," in line:
        parts = line.split(",")
        if len(parts) >= 2:
            last_name = parts[0].strip().title()
            first_name = parts[1].strip().title()
            return f"{first_name} {last_name}"
    
    # Handle "First Last" format with extra whitespace
    words = line.split()
    if not words:
        return None
    
    # Capitalize properly while keeping common surname particles lowercase
    particles = {"van", "de", "la", "von", "del", "di"}
    formatted_words = []
    for i, word in enumerate(words):
        if word.lower() in particles and i > 0:
            formatted_words.append(word.lower())
        else:
            formatted_words.append(word.capitalize())
    
    return " ".join(formatted_words)

def get_last_name(full_name):
    words = full_name.split()
    # Support compound last names with particles (e.g., "van Dijk")
    particles = {"van", "de", "la", "von", "del", "di"}
    if len(words) >= 2 and words[-2].lower() in particles:
        return f"{words[-2]} {words[-1]}"
    return words[-1]

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: '{INPUT_FILE}' not found.")
        return

    cleaned_names_set = set()

    # Load and clean names from the original file without modifying it
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            formatted_name = clean_and_format_name(line)
            if formatted_name:
                cleaned_names_set.add(formatted_name)

    # Sort the unique names alphabetically by last name
    sorted_names = sorted(list(cleaned_names_set), key=get_last_name)

    # Write the result to the new output file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for name in sorted_names:
            f.write(name + "\n")

    print(f"Success! Processed '{INPUT_FILE}' and wrote sorted results to '{OUTPUT_FILE}'.")

if __name__ == "__main__":
    main()