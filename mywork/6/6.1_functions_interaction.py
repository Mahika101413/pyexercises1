"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of monthly budget amounts.
# 2. Process, function by function:
#    - calculate_average(): Computes the arithmetic mean of the budget list.
#    - filter_above_threshold(): Selects items from the list that exceed a specific threshold.
#    - calculate_percentage(): Computes the percentage share of a subset sum relative to the total sum.
#    - Fourth function (get_above_average_share): Combines the three above to coordinate the workflow.
# 3. Out: A float representing the percentage of the total budget held by above-average expenses.
# 4. The question my fourth function answers: "What percentage of the total budget is concentrated in expenses that are above the average budget?" 
#    Splitting makes it easier to check because you can test each distinct step independently (mean calculation, filtering, percentage math) 
#    without hunting for bugs in a tangled, single monolithic block of code.

# TEST CASES FOR THE THREE SMALL FUNCTIONS:
# 1. calculate_average:
#    - Input: [100, 200, 300] -> Expected Output: 200.0
# 2. filter_above_threshold:
#    - Input: ([100, 200, 300], 150) -> Expected Output: [200, 300]
# 3. calculate_percentage:
#    - Input: (50, 200) -> Expected Output: 25.0

# Your code below
def calculate_average(numbers):
    """Computes the arithmetic mean of a list of numbers."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def filter_above_threshold(numbers, threshold):
    """Returns elements from a list that exceed a specified threshold."""
    return [num for num in numbers if num > threshold]


def calculate_percentage(part, total):
    """Calculates the percentage of a subset relative to a total."""
    if total == 0:
        return 0.0
    return (part / total) * 100


def get_above_average_share(budgets):
    """Answers: What percentage of the total budget is held by above-average expenses?
    Uses the three small functions sequentially.
    """
    if not budgets:
        return 0.0
        
    # Step 1: Find the average budget value
    avg_value = calculate_average(budgets)
    
    # Step 2: Filter budgets that are strictly greater than that average
    above_avg_budgets = filter_above_threshold(budgets, avg_value)
    
    # Step 3: Calculate the percentage share of those filtered budgets relative to the total
    total_sum = sum(budgets)
    subset_sum = sum(above_avg_budgets)
    percentage = calculate_percentage(subset_sum, total_sum)
    
    return percentage


# Our original dataset from Exercise 4.1
monthly_budgets = [1200, 950, 600, 450, 200, 1500, 800, 300]

# Run the fourth combined function
final_result = get_above_average_share(monthly_budgets)

# Display the final answer
print(f"Monthly Budgets: {monthly_budgets}")
print(f"Percentage of total budget held by above-average expenses: {final_result:.1f}%")