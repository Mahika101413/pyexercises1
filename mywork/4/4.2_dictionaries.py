"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A dictionary defining a specific digital marketing campaign with five key operational attributes.
# 2. Process: The program reads specific dictionary fields, modifies values, removes an obsolete field, safely handles a non-existent field lookup to prevent a KeyError, and iterates through to display every remaining field.
# 3. Out: Formatted console outputs showing initial inspection, updates, removal, safe error-free handling of a missing key, and the final state of all key-value pairs.
# 4. My object, my five fields, and why those:
#    - Object: A digital marketing campaign ("Summer Sale 2026").
#    - Five fields: `name`, `channel`, `budget`, `status`, and `clicks`.
#    - Why those: These are core metadata and performance descriptors used daily in marketing operations to track financial allocation, channel placement, operational status, and user engagement.


# Your code below
# Define the dictionary representing the marketing campaign object
campaign = {
    "name": "Summer Sale 2026",
    "channel": "Paid Search",
    "budget": 1200,
    "status": "Active",
    "clicks": 4500
}

# 1. Read the initial object
print("--- 1. Initial Campaign Object ---")
print(campaign)
print()

# Read specific fields
print("--- 2. Reading Specific Fields ---")
print(f"Campaign Name: {campaign['name']}")
print(f"Active Channel: {campaign['channel']}")
print()

# 2. Change it (modify budget and status)
print("--- 3. Changing Fields ---")
campaign["budget"] = 1500  # Increased budget
campaign["status"] = "Optimized"
print(f"Updated Budget: €{campaign['budget']}")
print(f"Updated Status: {campaign['status']}")
print()

# 3. Remove one field (e.g., removing 'clicks' to replace it with conversion metrics)
print("--- 4. Removing a Field ---")
removed_clicks = campaign.pop("clicks")
print(f"Removed field 'clicks' (previous value: {removed_clicks})")
print()

# Check it yourself: 
# Note: Trying to access a non-existent key directly like `campaign["roi"]` 
# raises a KeyError and crashes the program. We make it survive that case 
# using the dictionary `.get()` method or a conditional try-except block.
print("--- 5. Safe Query for a Non-Existent Field ---")
missing_field = "roi"
safe_result = campaign.get(missing_field, "Field not found (survived KeyError)")
print(f"Attempting to read '{missing_field}': {safe_result}")
print()

# 4. Display every remaining field with its value
print("--- 6. Final Display of All Fields ---")
for key, value in campaign.items():
    print(f"{key}: {value}")