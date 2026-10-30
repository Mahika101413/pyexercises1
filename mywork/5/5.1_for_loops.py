"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of monthly budget amounts (monthly_budgets = [1200, 950, 600, 450, 200, 1500, 800, 300]).
# 2. Process: We calculate the total sum of the budgets, then iterate through the list using enumerate() 
#    to track each item's 1-based position and value. For each item, we compute its percentage share of the 
#    total and check if it exceeds a $500 threshold.
# 3. Out: A printed line for every item combining its rank position, original budget amount, percentage 
#    share of the total, and whether it passes the $500 threshold.
# 4. What I compute for each item, and why it is worth showing: We compute each item's share of the 
#    total budget and a threshold check. The reader learns the relative weight of each individual 
#    expense against the overall total.


# Your code below

monthly_budgets = [1200, 950, 600, 450, 200, 1500, 800, 300]

# Calculate the total budget sum to use for share calculations
total_budget = sum(monthly_budgets)

# Loop through the list using enumerate with start=1 to avoid off-by-one indexing for human readability
for position, budget in enumerate(monthly_budgets, start=1):
    # Compute the share of the total (formatted to 1 decimal place)
    share = (budget / total_budget) * 100
    
    # Check if the budget passes our $500 threshold
    is_high_budget = budget > 500
    
    # Display the combined line
    print(f"Position {position}: ${budget} accounts for {share:.1f}% of the total. Above $500 threshold? {is_high_budget}")