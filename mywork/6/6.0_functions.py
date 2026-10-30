"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of numerical budget values.
# 2. Process: The function checks if the list is empty to prevent errors, calculates the sum of 
#    all items, counts the items, and computes the average budget value.
# 3. Out: A float representing the calculated average budget (returned, not printed).
# 4. My function name, and why return rather than print: 
#    - Function name: calculate_average_budget (clearly and accurately describes what the function does).
#    - Why return vs print: Returning allows us to store the result in a variable, reuse it in 
#      subsequent calculations, or format it later. Printing only outputs text to the console and 
#      yields None, turning the function into a dead-end that cannot be integrated into larger workflows.
#    - Empty list behavior: If passed an empty list, division by zero would occur unless handled. 
#      Adding a guard check (if not budget_list: return 0.0) makes this safe, which is robust and acceptable behavior.


# Your code below
def calculate_average_budget(budget_list):
    """Calculates and returns the average amount from a list of budgets.
    Includes a safety check for empty lists to prevent ZeroDivisionError.
    """
    if not budget_list:
        return 0.0
    
    total = sum(budget_list)
    count = len(budget_list)
    return total / count


# Our original list from Exercise 4.0
monthly_budgets = [1200, 950, 600, 450, 200, 1500, 800, 300]

# Call the function three times with different inputs:
result_full = calculate_average_budget(monthly_budgets)       # 1. Full original list
result_subset_1 = calculate_average_budget([1200, 950, 600])  # 2. First subset of budgets
result_subset_2 = calculate_average_budget([450, 200, 1500])  # 3. Second subset of budgets

# Display the three results
print(f"1. Average of full monthly budgets list: ${result_full:.2f}")
print(f"2. Average of first subset: ${result_subset_1:.2f}")
print(f"3. Average of second subset: ${result_subset_2:.2f}")

# Optional check with an empty list
empty_result = calculate_average_budget([])
print(f"4. Average of an empty list (safely handled): ${empty_result:.2f}")
# The Emplty List exception was safely handled.