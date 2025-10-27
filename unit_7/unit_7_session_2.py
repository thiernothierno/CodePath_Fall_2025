
# Problem 1: Find Millenium Falcon Part
# Understand
# Is the given list always sorted?
# What should we do when the input has no element?
# What about if a match is not found?

# Plan
# Use binary search approach
# Return False if len(stock) equal 0.
# Declare two variables low and high pointing the first and last index in the stock list respectively.
# Find the middle element.
# Start comparaison:
# if middle element equal to the value we are looking for, return True
# Decrease the high variable by 1, when value in the middle is greater than the value at index low.
# Otherwise, increase the low variable by 1.
# Return false if no match found.
# Time Complexity: O(log N) because we are performing binary search on the inventory array.
# Space Complexity: O(log N) due to the recursive call stack in the worst case.

# Implement
def check_stock(inventory, part_id):
    """Return True if the part_id is in inventory and False otherwise."""
    if len(inventory) == 0:
        return False
    low, high = 0, len(inventory) - 1
    while low <= high:
        middle = (low + high) // 2
        if inventory[middle] == part_id:
            return True
        elif inventory[middle] > part_id:
            high -= 1
        else:
            low += 1
    return False


print("\nOutput of Problem 1: ")
print(check_stock([1, 2, 5, 12, 20], 20))  # Output: True
print(check_stock([1, 2, 5, 12, 20], 100))  # Output: False


# Problem 2: Find Millenium Falcon Part I
# Understand
# Is the given list always sorted?
# What should we do when the input has no element?
# What about if a match is not found?

# Plan
# Define a helper function that takes four parameter, list, target, low , high.
# Inside the helper function do the following:
# base case: return False when low > high.
# Find middle element.
# if value at middle index equal to target, return True.
# if value at middle index > target, recursively return helper(list, target, low, high-1)
# else: return helper(list, target, low+1, high)
# call the helper function inside the main function with low and high respectively: 0 and len(list)-1
# Time Complexity: O(log N) because we are performing binary search on the inventory array.
# Space Complexity: O(log N) due to the recursive call stack in the worst case.

# Implement
def check_stock_recursive(inventory, part_id):
    """Return True if the part_id is in inventory and False otherwise."""
    def helper(my_list, target, low, high):
        if low > high:
            return False
        middle = (low + high) // 2
        if my_list[middle] == target:
            return True
        elif my_list[middle] > target:
            return helper(my_list, target, low, high-1)
        else:
            return helper(my_list, target, low+1, high)

    return helper(inventory, part_id, 0, len(inventory) - 1)


print("\nOutput of Problem 2: ")
print(check_stock_recursive([1, 2, 5, 12, 20], 1))  # Output: True
print(check_stock_recursive([1, 2, 5, 12, 20], 120))  # Output: False


# Problem 3: Find First and Last Frequency Positions

# Understand
# Is the array always sorted?
# What should we do when the target value appears only once in the array?
# What should we do when the array is empty or no target is given?
# Is there a time or space complexity constraint?

# Plan
# Define two helper functions to find the first and last occurance of the target value.
# First helper function:
# Declare two variable low and high equal to 0 and len(list)-1 respectively.
# Define a variable value = -1
# Find middle element between low and high.
# if value at middle equal target value, update value equal to middle
# if value at middle greater than or equal to target, decrease high variable by 1.
# Otherwise, increase low variable by 1.
# Return value.
# Last helper function.
# Do the same as in the first helper function. But change the way a update variables.
# Inside main function.
# return (value_1, value_2) if value_1 not equal to -1, else : return (-1,-1)
# Time Complexity: O(log N) because we are performing binary search on each helper function.
# Space Complexity: O(1) since we are using variables to store our result.
# Implement
def find_frequency_positions(transmissions, target_code):
    # Helper function to find the first occurance of target value.
    def first_frequency_positions(transmissions, target_code):
        """returns a tuple with the first and last indices of a specific frequency code target_code in transmissions. 
        If target_code does not exist in transmissions, return (-1, -1)."""
        low, high = 0, len(transmissions)-1
        first_position = -1
        while low <= high:
            middle = (low + high) // 2
            if transmissions[middle] == target_code:
                first_position = middle
            if transmissions[middle] >= target_code:
                high -= 1
            else:
                low += 1
        return first_position

    # Helper function to find last occurance of target value.
    def last_frequency_positions(transmissions, target_code):
        """returns a tuple with the first and last indices of a specific frequency code target_code in transmissions. 
        If target_code does not exist in transmissions, return (-1, -1)."""
        low, high = 0, len(transmissions)-1
        last_position = -1
        while low <= high:
            middle = (low + high) // 2
            if transmissions[middle] == target_code:
                last_position = middle
            if transmissions[middle] <= target_code:
                low += 1
            else:
                high -= 1
        return last_position
    first = first_frequency_positions(transmissions, target_code)
    last = last_frequency_positions(transmissions, target_code)

    if last != -1 or first != -1:
        return (first, last)
    else:
        return (-1, -1)


print("\nOutput of Problem 3:")
print(find_frequency_positions([5, 7, 7, 8, 8, 10], 8))  # Output: (3,4)
print(find_frequency_positions([5, 7, 7, 8, 8, 10], 6))  # Output : (-1, -1)
print(find_frequency_positions([], 0))  # Output: (-1, -1)
