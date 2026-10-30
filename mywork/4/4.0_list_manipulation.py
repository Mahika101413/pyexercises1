"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of 8 integers representing monthly marketing budgets (in EUR) allocated across different acquisition channels.
# 2. Process: The program prints the original list, accesses a specific item by index, generates and displays a sorted copy of the list, and computes both the total expenditure and the average budget per channel.
# 3. Out: Clear console prints displaying the raw list, a chosen individual item, the sorted list, and the computed totals/averages.
# 4. What my list is about, and what I computed from it: The list tracks monthly financial allocations for 8 distinct marketing channels. I computed the total monthly marketing spend and the average channel budget. This total is interesting because it immediately highlights our total monthly burn rate for customer acquisition and ensures we stay within the financial cap.

# Define the list of monthly budgets (in EUR) for 8


# Your code below
# Define the list of monthly budgets (in EUR) for 8 channels
monthly_budgets = [1200, 950, 600, 450, 200, 1500, 800, 300]

# 1. Display the whole list
print("--- 1. Whole List ---")
print(f"All monthly budgets: {monthly_budgets}")
print()

# 2. Display one item of your choice (e.g., index 2, representing the 3rd channel)
print("--- 2. Single Item of Choice ---")
chosen_index = 2
print(f"Budget for the channel at index {chosen_index}: €{monthly_budgets[chosen_index]}")
print()

# 3. Display the list sorted
print("--- 3. Sorted List ---")
sorted_budgets = sorted(monthly_budgets)
print(f"Sorted budgets (ascending): {sorted_budgets}")
print()

# 4. Display something computed from it (Total and Average)
print("--- 4. Computed Data ---")
total_budget = sum(monthly_budgets)
average_budget = total_budget / len(monthly_budgets)
print(f"Total monthly marketing budget: €{total_budget}")
print(f"Average budget per channel: €{average_budget:.2f}")