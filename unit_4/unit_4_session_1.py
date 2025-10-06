
# Standard Problem Set Version 2:
# Problem 7: Search for Viral Meme Groups
"""The problem will help understand how to unpack element from a given list of tuple and how to apply the two pointer technique."""

# Understand
# Is it guaranteed that the given list is sorted?
# What should we return when the list is empty?
# What should we do when the target is not far off the given values?
# Is there a time or space complexity constraint?

# Plan
# Declare an empty tuple curr_pair that store the current closest pair.
# Define a variable max_sum, and set it to +inf
# Define another variable max_sum to track how we should move our pointer.
# Define two pointers left and right, respectively pointing to first and last index of the given list.
# Iterate over the given list, while left pointer is less than right pointer do the following:
# Add current values of left and right and store to a variable curr_sum.
# Find the absolute difference between target and curr_sum and store it into a variable curr_diff.
# Update max_sum to curr_diff if curr_diff is less than max_sum. Store current name into curr_pair.
# Decrement right pointer by 1 if curr_sum is greater than target.
# Increment left pointer by 1 if curr_sum is less than target.
# Return curr_pair.
# Time Complexity is O(n) since we need to move our pointers at most n-1.
# Space Complexity is O(1) since we are using only variables to store our data.

# Implement


def find_closest_meme_pair(memes, target):
    """Return the names of the two memes whose combined popularity score is closest to the target."""
    curr_pair = ()
    max_sum = float('inf')
    left = 0
    right = len(memes) - 1
    while left < right:
        meme1, val1 = memes[left]
        meme2, val2 = memes[right]
        curr_sum = val1 + val2
        curr_diff = abs(target - curr_sum)
        if curr_diff < max_sum:
            max_sum = curr_diff
            curr_pair = (meme1, meme2)
        if curr_sum > target:
            right -= 1
        else:
            left += 1
    return curr_pair


print("\nOutput Problem 1:")
memes_1 = [("Distracted boyfriend", 5), ("Dogecoin to the moon!", 7),
           ("One does not simply walk into Mordor", 12)]
memes_2 = [("Surprised Pikachu", 2), ("This is fine", 6),
           ("Expanding brain", 9), ("Y U No?", 15)]
memes_3 = [("Philosoraptor", 1), ("Bad Luck Brian", 4),
           ("First world problems", 8), ("Y U No?", 13)]

print(find_closest_meme_pair(memes_1, 13))
print(find_closest_meme_pair(memes_2, 10))
print(find_closest_meme_pair(memes_3, 12))


# Problem 8: Analyze Meme Trends
"""This problem demonstrate how to perform slicing, and data interpretation with algorithmic reasoning."""
# Understand
# What should we do when the given range is out of bound from the given list of scores?
# What should we do when memes is None?
# Is there a time or space complexity constraint?

# Plan
# Define an empty string res to store the final output.
# Declare a variable max_sum and set it to -inf.
# Loop through the given list, and unpack and store the memes['name'] and memes['reposts] into a variable name and repost.
# Return [] if start_day < 0 or end_day > len(memes).
# Iterate over the given range, and add their corresponding values.
# Find the average, and update max_sum when average > max_sum. Thwn store current name into res.
# Return res.
# Time Complexity is O(n * k) .Outer loop → runs n times (once per meme). Inner loop (summing reposts) → runs k times (one per day in range)
# Space Complexity is O(1) since we are using only variables to store our data.

# Implement


def find_trending_meme(memes, start_day, end_day):
    """Return the name of the meme with the highest average reposts over the specified period"""
    if not memes:
        return []
    res = ""
    max_sum = float('-inf')
    for meme in memes:
        name = meme['name']
        repost = meme['reposts']
        n = len(repost)
        if start_day < 0 or end_day >= n:
            return None

        diff = end_day - start_day + 1
        total = 0
        for i in range(start_day, end_day + 1):
            total += repost[i]

        average = total / diff
        if average > max_sum:
            max_sum = average
            res = name

    return res


print("\nOutput Problem 2:")

memes = [
    {"name": "Distracted boyfriend", "reposts": [5, 3, 2, 7, 6]},
    {"name": "Dogecoin to the moon!", "reposts": [2, 4, 6, 8, 10]},
    {"name": "One does not simply walk into Mordor",
        "reposts": [3, 3, 5, 4, 2]}
]

memes_2 = [
    {"name": "Surprised Pikachu", "reposts": [2, 1, 4, 5, 3]},
    {"name": "This is fine", "reposts": [3, 5, 2, 6, 4]},
    {"name": "Expanding brain", "reposts": [4, 2, 1, 4, 2]}
]

memes_3 = [
    {"name": "Y U No?", "reposts": [1, 2, 1, 2, 1]},
    {"name": "Philosoraptor", "reposts": [3, 1, 3, 1, 3]}
]
print(find_trending_meme(memes, 1, 3))
print(find_trending_meme(memes_2, 0, 2))
print(find_trending_meme(memes_3, 2, 4))

# Advanced Problem Set Version 1
# Problem 7: Calculate Fabric Waste
"""This problem is great for understanding techniques such as looping, and slicing"""
# Understand
# What should we do when the length of parameters are not the same?
# What should we do when one of the given parameter is empty?
# Is there a time or space complexity constraint?

# Plan
# Define a variable total to store the final output.
# Loop over the list of items and do the following:
# Store the second value of the tuple to a variable called value.
# Store the value of the current index of the fabric_rolls to a variable rolls.
# Add the absolute difference of rolls and value, and store it in total.
# Return total.
# Time Complexity is O(n) since we need to scan all element in items.
# Space Complexity is O(1) since we are using only variables to store our data.
# Implement


def calculate_fabric_waste(items, fabric_rolls):
    """Return the total fabric waste after producing all the items"""
    total = 0
    for i in range(len(items)):
        value = items[i][1]
        rolls = fabric_rolls[i]
        total += abs(rolls - value)
    return total


print("\nOutput Problem 3:")

items = [("T-Shirt", 2), ("Pants", 3), ("Jacket", 5)]
fabric_rolls1 = [5, 5, 5]

items_2 = [("Dress", 4), ("Skirt", 3), ("Blouse", 2)]
fabric_rolls2 = [4, 4, 4]

items_3 = [("Jacket", 6), ("Shirt", 2), ("Shorts", 3)]
fabric_rolls3 = [7, 5, 5]

print(calculate_fabric_waste(items, fabric_rolls1))
print(calculate_fabric_waste(items_2, fabric_rolls2))
print(calculate_fabric_waste(items_3, fabric_rolls3))
