"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In: User input for a student's first name, last name, email address, and student number.
# 2. Process: Validate inputs (ensure strings are not empty and the email contains an '@' symbol), 
#    check if `7.0_student_data.csv` already exists; if not, create it and write the semicolon-separated 
#    header row. Then, append the validated entry as a new row without overwriting existing data.
# 3. Out, file name and columns: File name: `7.0_student_data.csv`. Columns: first_name;last_name;email;student_number
# 4. Why these columns, and what this file is for: I chose these columns to register students for a course or workshop 
#    and keep track of their contact and identification details. Once the file has two hundred rows, I would import 
#    it into a course management tool or mailing system to send out course materials, organize study groups, and 
#    track attendance.

# Your code below
import os
import csv

FILENAME = "7.0_student_data.csv"

def get_valid_first_name():
    while True:
        first_name = input("Enter student's first name: ").strip()
        if first_name:
            return first_name
        print("Error: First name cannot be empty. Please try again.")

def get_valid_last_name():
    while True:
        last_name = input("Enter student's last name: ").strip()
        if last_name:
            return last_name
        print("Error: Last name cannot be empty. Please try again.")

def get_valid_email():
    while True:
        email = input("Enter student's email address: ").strip()
        if "@" in email and "." in email.split("@")[-1]:
            return email
        print("Error: Invalid email format. Please include an '@' and a valid domain.")

def get_valid_student_number():
    while True:
        student_number = input("Enter student number (digits only): ").strip()
        if student_number.isdigit():
            return student_number
        print("Error: Student number must contain only digits. Please try again.")

def main():
    print("--- Student Data Entry ---")
    first_name = get_valid_first_name()
    last_name = get_valid_last_name()
    email = get_valid_email()
    student_number = get_valid_student_number()

    entry = [first_name, last_name, email, student_number]
    
    # Check if the file exists already to determine whether we need to write a header
    file_exists = os.path.exists(FILENAME)

    # Open file in append mode ('a') with semicolon delimiter to match 7.0_student_data.csv format
    with open(FILENAME, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        
        # If the file didn't exist before opening, write the header row first
        if not file_exists:
            writer.writerow(["first_name", "last_name", "email", "student_number"])
            
        writer.writerow(entry)

    print(f"\nSuccess! Entry saved to '{FILENAME}'.")

if __name__ == "__main__":
    main()