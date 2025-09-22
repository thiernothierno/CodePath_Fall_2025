

# Advanced Problem Set Version 1
# Problem 1: Balanced Art Collection

# This problem will help understand the concept of subsequent, how to add element into an empty dictionary.

# Understand
# Does the given list contain duplicate values?
# What should we return when the list is empty?
# Are elements in the list ordered?
# Is there a time or space complexity constraint?

# Plan
# Have a dictionary num that will store the frequency of each element in the list.
# Define a max_length variable initially 0, to store the final output.
# Loop through the num dictionary:
# Check if num + 1 exist in dictionary num:
# Store the length of num and num + 1 to a variable current_length.
# Update max_length if current_length is greater than max_length.
# Return max_length

# Implement

def find_balanced_subsequence(art_pieces):
    """Function that returns the length of the longest balanced subsequence"""
    my_dictionary = {}
    max_length = 0
    for art in art_pieces:
        if art in my_dictionary:
            my_dictionary[art] += 1

        else:
            my_dictionary[art] = 1

    for val in my_dictionary:
        if val + 1 in my_dictionary:
            current_length = my_dictionary[val] + my_dictionary[val + 1]

            max_length = max(max_length, current_length)

    return max_length


art_pieces1 = [1, 3, 2, 2, 5, 2, 3, 7]
art_pieces2 = [1, 2, 3, 4]
art_pieces3 = [1, 1, 1, 1]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))


# Problem 2: Verifying Authenticity
# I picked this problem because it will helps students learn the concept of permutation which is a concept widely used in computer science.

# Understand
# What the format of the given input? strings? integers?
# WHat does it mean by base[n]?

# Plan
# find the max number of the given list and store it in a variable called n.
# Return false if n is not equal to len(art_pieces) + 1.
# Define an empty dictionary callded dictionary.
# Add all elements of art_pieces into the dictionary value with their corresponding frequencies.
# Check if dictionary matched the base n structure.
# Each number for 1 to n-1 should appear exactly once, and n twice.
# Return True if condition is satisfied.

# Implement

def is_authentic_collection(art_pieces):
    """Returns True if the given array is an authentic array, and otherwise returns False."""
    n = max(art_pieces)

    if n + 1 != len(art_pieces):
        return False

    dictionary = {}
    for val in art_pieces:
        if val in dictionary:
            dictionary[val] += 1
        else:
            dictionary[val] = 1

    for i in range(1, n):
        if dictionary.get(i, 0) != 1:
            return False

    return dictionary.get(n, 0) == 2


collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))


# Problem 1: Filter Destinations
# This problem will help to understand how to access values in a dictionary and compare them with a given threshold.

# Understand
# What should we return when the rating_threshold is greater than all value in destionation?
# WHat should we return when destination is empty?
# Is there a time or space complexity constraint?

# Plan
# Define an empty dictionary result.
# Loop through the destinations dictionary.
# Add the corresponding key, value into result dictionary if value is greater than threshold.
# Return result

# Implement

def remove_low_rated_destinations(destinations, rating_threshold):
    """Return the updated dictionary after removing all values in the destionation strickly less that rating_threshold."""
    result = {}
    for key, val in destinations.items():
        if val > rating_threshold:
            result[key] = val

    return result


destinations = {"Paris": 4.8, "Berlin": 3.5, "Addis Ababa": 4.9, "Moscow": 2.8}
destinations2 = {"Bogotá": 4.8, "Kansas City": 3.9,
                 "Tokyo": 4.5, "Sydney": 3.0}

print(remove_low_rated_destinations(destinations, 4.0))
print(remove_low_rated_destinations(destinations2, 4.9))
