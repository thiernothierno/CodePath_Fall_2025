

# Advanced Problem Set Version 1: Problem 2: Build the Tallest Skyscraper
"""This problem help how to compare adjacent element using stack."""
# Understand
# Is the input format always positive integers?
# What should we return when the given floors is empty?
# Is there a time or space complexity constraint?

# Plan
# Declare a stack to track the number of skyscrapers we can build.
# Define a count variable that will store the final output.
# Loop through the list of floors and do the following:
# Starting adding element in stack when stack is empty, and increment count by 1 to mark the start of a new skyscraper.
# Continue adding element into stack when top of stack is greater than or equal to current floor.
# IF top of stack is less than current floor, remove element from stack till condition is no longer valid.
# THen add element to stack and increment count to start building a new skyscraper.
# Return count.
# Implement


def build_skyscrapers(floors):
    """Return the number of skyscrapers you can build using the given floors."""
    stack = []
    count = 0

    for floor in floors:

        if not stack:
            stack.append(floor)
            count += 1

        elif stack[-1] >= floor:
            stack.append(floor)

        elif stack[-1] < floor:
            while stack and stack[-1] < floor:
                stack.pop()

            stack.append(floor)
            count += 1

    return count


print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9]))
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2]))


# Problem 7: Next Greater Element
"""This problem will help understand how to access element of an array in a circular motion using the modulo operator."""
# Understand
# Does the array contain only integers?
# What should we do when the array is empty?
# Is there a time or space complexity constraint?

# Plan
# Define a result array of size of n, and initialize it with -1.
# Define a stack to keep track index of elements.
# Loop through twice over the array to hande the circular nature.
# Define an index variable that will wrap around the array using the modulo operator.
# pop element from stack if current is greater.
# Push element in stack only during the first pass.
# Return result.
# Implement


def next_greater_dream(dreams):
    """Return next greater element if it exist, otherwise, return -1."""
    n = len(dreams)
    stack = []
    result = [-1] * n
    for i in range(n * 2):
        index = i % n

        while stack and dreams[stack[-1]] < dreams[index]:
            prev_val = stack.pop()
            result[prev_val] = dreams[index]

        if i < n:
            stack.append(index)
    return result


print(next_greater_dream([1, 2, 1]))
print(next_greater_dream([1, 2, 3, 4, 3]))


# Standard Problem Set Version 2: Problem 2: Find First Symmetrical Landmark Name
"""I picked this problem because it requires a combination of learning the two pointer technique and how to define and work with helper function. """

# Understand
# What the output format should look like?
# What does it mean to a word to be symmetrical?
# Is there a time or space complexity constraint?

# Plan
# Define a helper function that will return true if word is symmetrical or not.
# Inside the helper function, declare two pointers left and right pointing respectivelly to 0 and len(words) - 1.
# while the left point is less than the right pointer, return false if their corresponding char is not the same.
# Otherwise, increment left pointer by 1, and decrement right pointer by 1.
# Return True if condition is satisfied.
# Outside the helper function, iterate over the given landmark,
# For each word, return word if it symmetrical.
# If no match found, return ''.

# Implement


def first_symmetrical_landmark(landmarks):
    """return the first symmetrical landmark name. If there is no such name, return an empty string."""
    def is_symmetric(word):
        left = 0
        right = len(word) - 1
        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1

        return True
    for landmark in landmarks:
        if is_symmetric(landmark):
            return landmark

    return ''


print(first_symmetrical_landmark(["canyon", "forest", "rotor", "mountain"]))
print(first_symmetrical_landmark(["plateau", "valley", "cliff", "racecar"]))
