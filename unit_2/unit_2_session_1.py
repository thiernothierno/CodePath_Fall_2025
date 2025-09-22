
# Advanced Problem Set Version 2
# Problem 1: The Library of Alexandria

# This problem will help student understand how to access element (keys, values) in a dictionnary, how to perform arithmetic operation with two differents dictionaries.


# Understand
# What should we return when on of the given dictionary is empty?
# Does both dictionary have the same size?
# Are the keys in both dictonaries same and in order?
# Is there a time or space complexity constraint?

# Plan
# Return dict_1 if len(dict_2) is 0, or return dict_2 if len(dict_1) is 0.
# Define an empty output dictionary to store the result.
# Iterate over the library catalog,
# For each key, store it correspondant value into a variable called expected_val.
# Store each value of the actual distribution into a variable called actual_val.
# Store the difference of actual_val and expected val into the output result.

# # Implement

def analyze_library(library_catalog, actual_distribution):
    """Function that return a dictionary where the keys are the room names and the values are the differences in the number of scrolls
    (actual number of scrolls - expected number of scrolls)"""
    output = {}
    for key in library_catalog.keys():
        expected_val = library_catalog[key]
        actual_val = actual_distribution[key]
        output[key] = actual_val - expected_val

    return output


library_catalog = {
    "Room A": 150,
    "Room B": 200,
    "Room C": 250,
    "Room D": 300
}

actual_distribution = {
    "Room A": 150,
    "Room B": 190,
    "Room C": 260,
    "Room D": 300
}


print(analyze_library(library_catalog, actual_distribution))


# Problem 2: Grecian Artifacts
# I picked this problem because it will help how to access element in a list, and how to use python method such as the append() to add element in a list.

# Understand
# What should we return when one of the list is empty?
# Are we allowed to use python built-in methods?
# Is there a time or space complexity constraint?

# Plan
# Return list_1 if list_2 is empty or return list_2 if list_1 is empty.
# Define an empty result list to store the output.
# Loop through actifacts1.
# for each element in actifacts1, add it to result if it present in actifacts2.

# Return result.

# Implement

def find_common_artifacts(artifacts1, artifacts2):
    """Function that returns a list of artifacts common to both time periods."""
    result = []
    for artifacts in artifacts1:
        if artifacts in artifacts2:
            result.append(artifacts)

    return result


artifacts1 = ["Statue of Zeus", "Golden Vase", "Bronze Shield"]
artifacts2 = ["Golden Vase", "Silver Sword", "Bronze Shield"]

print(find_common_artifacts(artifacts1, artifacts2))


# Problem 4: Time Portals
# This problem will help understand how to concatenate strings, and how to check condition in a nested loop.

# Understand
# What should we do when the given list is empty?
# Is it guaranteed that all element present are strings?
# Is there a time or space complexity constraint?

# Plan
# Define a count variable to store the final output.
# Use i,j and loop through the range of the length of portals.
# Check if i != j
# increment count by 1, if destination equal portals[i] + portals[j]

# Return count
# Implement

def num_of_time_portals(portals, destination):
    """ Return the number of pairs of indices (i, j) (where i != j) 
    such that the concatenation of portals[i] + portals[j] equals destination."""
    count = 0
    n = len(portals)
    for i in range(n):
        for j in range(n):
            if i != j:
                if destination == portals[i] + "" + portals[j]:
                    count += 1
    return count


portals1 = ["777", "7", "77", "77"]
destination1 = "7777"
portals2 = ["123", "4", "12", "34"]
destination2 = "1234"
portals3 = ["1", "1", "1"]
destination3 = "11"

print(num_of_time_portals(portals1, destination1))
print(num_of_time_portals(portals2, destination2))
print(num_of_time_portals(portals3, destination3))
