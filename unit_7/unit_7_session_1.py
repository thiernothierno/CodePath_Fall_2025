# 2 Advanced Problem Set Version 1 and 1 standard problem set version 1

# Problem 1: Counting the Layers of a Sandwich
# Understand
# Is the given input always in a list format?
# Is the list consist a neested list?
# Is there a time or space complexity constraint?
# What should we do when the list is empty or contain only 1 element?

# Plan
# Check for base cases, return 0 when the length of the list is 0, and 1 when it equal to 1.
# Recursively return 1 + count_layers(list[1])
# Time complexity: O(n)
# Space complexity: O(n)
# Implement
def count_layers(sandwich):
    """Function that returns the total number of sandwich layers."""
    if len(sandwich) == 0:
        return 0
    if len(sandwich) == 1:
        return 1

    return 1 + count_layers(sandwich[1])


sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

print("\nOutput of Problem 1:")
print(count_layers(sandwich1))
print(count_layers(sandwich2))


# Problem 2: Reversing Deli Orders
# Understand
# Is the given input a list or a tuple?
# What the output format should look like?
# Is there a time or space complexity constraint?
#
# Plan
# Define a helper function that will serve to reverse the given input.
# Inside the helper function:
# Check base cases: return an empty string when len(orders) equal 0.
# Base case: return the element at index 0, when len(orders) equal 1.
# Recursively return helper(order[1:]) + " " + order[0]
# Inside the main function:
# Split the given input into a list format and save it to a variable call word.
# call the helper function passing the word variable as parameter.
# Time complexity: O(n)
# Space complexity: O(n)
# Implement

def reverse_helper(orders):
    """Function that reverse elements in a list"""
    if len(orders) == 0:
        return []
    if len(orders) == 1:
        return orders[0]

    return reverse_helper(orders[1:]) + " " + orders[0]


def reverse_order(words):
    word = words.split()
    return reverse_helper(word)


order = ("Bagel Sandwich Coffee")
print("\nOutput of Problem 2:")
print(reverse_order(order))


# Problem 1: Counting Iron Man's Suits
# Understand
# What is the format of the input? list? tuple?
# Is there a time or space complexity constraint?
#
# Plan
# Implement
def count_suits_iterative(suits):
    """Iteratively count the total number of suits in the list."""
    # Define a variable to count, initialize it to 0.
    count = 0
    # Iterate over the list, and increase count variable by 1.
    for suit in suits:
        count += 1
    # Return count
    return count


def count_suits_recursive(suits):
    """Recursively count the total number of suits in the list."""
    # Check for base case.
    if len(suits) == 0:
        return 0
    # Recursively return 1 + the count of the remaining element in the list.
    return 1 + count_suits_iterative(suits[1:])


print("\nOutput of Problem 3:")
print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))
