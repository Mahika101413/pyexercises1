"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The original list of 8 integers representing monthly marketing budgets from Exercise 4.0.
# 2. Process: Displaying the list in four distinct orders using non-destructive methods (like `sorted()` and slicing `[::-1]`) to protect the original data structure.
# 3. Out: Console printouts showing the four ordered variations, followed by a final verification print of the untouched original list.
# 4. My four orders, and which ones modify the original: 
#    - Orders chosen: (1) Original order, (2) Ascending sorted order, (3) Descending sorted order, and (4) Reversed order.
#    - In-place modifiers (modify the original): List methods `.sort()` and `.reverse()`.
#    - Non-destructive (return a new list/copy): Built-in function `sorted()` and slice notation `[::-1]`.

# Your code below
# Original list from Exercise 4.0
monthly_budgets = [1200, 950, 600, 450, 200, 1500, 800, 300]

# Order 1: Original order
print("--- 1. Original Order ---")
print(monthly_budgets)
print()

# Order 2: Sorted ascending
print("--- 2. Sorted Ascending (using sorted()) ---")
# sorted() returns a new list, leaving monthly_budgets untouched
print(sorted(monthly_budgets))
print()

# Order 3: Sorted descending
print("--- 3. Sorted Descending (using sorted(..., reverse=True)) ---")
# sorted() with reverse=True returns a new list, leaving monthly_budgets untouched
print(sorted(monthly_budgets, reverse=True))
print()

# Order 4: Reversed order
print("--- 4. Reversed Order (using slice [::-1]) ---")
# Slicing creates a new list copy in reverse order, leaving monthly_budgets untouched
print(monthly_budgets[::-1])
print()

# Final Verification: Prove the original list has not changed
print("--- Final Verification: Original List Unchanged ---")
print(monthly_budgets)