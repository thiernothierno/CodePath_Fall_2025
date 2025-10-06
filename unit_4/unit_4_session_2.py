
# Advanced Problem Set Version 1
# Problem 7: Identify Repeated Themes
"""This is a great problem because it demonstrates how to create, access and iterate over dictionaries. """
# Understand
# What should we return when the given list is empty?
# How the format of the output should be?
# Is there a time or space complexity constraint?

# Plan
# Define a dictionary to store element in a key, value pair format, where the key is the name, and the value is the frequency.
# Define a result list to store the final output.
# Loop over the given scenes, for each element set it value to 1 if it does not exist in the dictionary, otherwise, increment it frequency by 1.
# Loop over the dictionary, for any value greater than 1, append it corresponding name to the result list.
# Return result list.
# Time Complexity is O(n) since we need to scan all element in scenes.
# Space Complexity is O(n) because of the dictionary and result list we declared to store the data.

# Implement


def identify_repeated_themes(scenes):
    """Returns a list of these repeated themes."""
    res_map = {}
    output = []
    for scene in scenes:
        theme = scene['theme']
        if theme in res_map:
            res_map[theme] += 1
        else:
            res_map[theme] = 1

    for key, val in res_map.items():
        if val > 1:
            output.append(key)

    return output


print("\nOutput Problem 1:")

scenes = [
    {"scene": "The hero enters the dark forest.", "theme": "courage"},
    {"scene": "A mysterious figure appears.", "theme": "mystery"},
    {"scene": "The hero faces his fears.", "theme": "courage"},
    {"scene": "An eerie silence fills the air.", "theme": "mystery"},
    {"scene": "The hero finds a hidden treasure.", "theme": "discovery"}
]

repeated_themes = identify_repeated_themes(scenes)
print(repeated_themes)

scenes = [
    {"scene": "The spaceship lands on an alien planet.", "theme": "exploration"},
    {"scene": "A strange creature approaches.", "theme": "danger"},
    {"scene": "The crew explores the new world.", "theme": "exploration"},
    {"scene": "The crew encounters hostile forces.", "theme": "conflict"},
    {"scene": "The crew makes a narrow escape.", "theme": "danger"}
]

repeated_themes = identify_repeated_themes(scenes)
print(repeated_themes)

#  Problem 2: Find Most Wasted Food Item
"""This is a great problem because it demonstrates how to access and perform arithmetic operation on dictionary."""

# Understand
# What should we do when the given record is empty?
# How the output format should be?
# Is there a time or space complexity constraint?

# Plan
# Define a variable max_value that will track the maximum sum seeing so far.
# Declare an empty string name, initially empty to store the final output.
# Loop over the given records, store the sum of current list of record to a variable total.
# If total is greater than max_value, update max_value to total and store current record into string name.
# Return name.
# Time Complexity is O(n) since we need to scan all element in scenes.
# Space Complexity is O(1).
# Implement


def find_most_wasted_food_item(waste_records):
    """Function that return the most wasted food with highest frequency."""
    max_value = 0
    name = ""
    for record in waste_records:
        total = sum(waste_records[record])
        if total > max_value:
            max_value = total
            name = record
    return name


print("\nOutput Problem 2:")

waste_records1 = {
    "Apples": [200, 150, 50],
    "Bananas": [100, 200, 50],
    "Carrots": [150, 100, 200],
    "Tomatoes": [50, 50, 50]
}

result = find_most_wasted_food_item(waste_records1)
print(result)

waste_records2 = {
    "Bread": [300, 400],
    "Milk": [200, 150],
    "Cheese": [100, 200, 100],
    "Fruits": [400, 100]
}

result = find_most_wasted_food_item(waste_records2)
print(result)


# Problem 8: Manage Expiration Dates
"""This problem helps understand the stack data structure from declaring, checking condition, and pushing element. """

# Understand
# What should we do when the given list is empty?
# Is the given list always sorted?
# Is there a time or space complexity constraint?

# Plan
# Declare a stack
# Iterate over the given list.
# Check if stack and currend date is less than top of stack, then return False
# Othewise, append date to stack.
# Return True.
# Time Complexity is O(n) since we need to go through each element in expiration_dates..
# Space Complexity is O(n) because of the stack.

# Implement


def check_expiration_order(expiration_dates):
    """Return True if items are ordered correctly and False otherwise."""
    stack = []
    for order in expiration_dates:
        date = order[1]
        if stack and date < stack[-1]:
            return False
        else:
            stack.append(date)
    return True


print("\nOutput Problem 3:")

expiration_dates_1 = [
    ("Milk", "2024-08-05"),
    ("Bread", "2024-08-10"),
    ("Eggs", "2024-08-12"),
    ("Cheese", "2024-08-15")
]

expiration_dates_2 = [
    ("Cheese", "2024-08-15"),
    ("Bread", "2024-08-12"),
    ("Eggs", "2024-08-10"),
    ("Milk", "2024-08-05")
]

print(check_expiration_order(expiration_dates_1))
print(check_expiration_order(expiration_dates_2))
