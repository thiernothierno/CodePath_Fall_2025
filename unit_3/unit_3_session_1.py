

from collections import deque
# Problem 2: Reveal Attendee List in Order
"""I picked this problem because it helps demonstrate how to add and remove element from a queue."""

# Understand
# What should we return when the given list is empty?
# What should be the return output format?
# Is there a time or space complexity constraint?

# Plan
# Declare a result list of size len(attendees) to store the final output. Initially empty.
# Define a list index that will store the position of each attendees.
# Sort the given list of attendees in increasing order.
# Loop through the list of attendees and perform the following operations:
# Remove the first index position from the index list and assign it to a variable var.
# Append current attendee to result[var].
# If there are still element left in index list, move next element in the queue to the back of the queue.
# Return result.
# Time complexity: O(n) since we need to iterate through all elements in the attendees list.
# Space: O(n) because we create a result list to store the final output.


# Implement

def reveal_attendee_list_in_order(attendees):
    """returns an array with the correct starting order"""
    attendees = sorted(attendees)
    index_queue = deque(range(len(attendees)))
    result = [0] * len(attendees)
    for attendee in attendees:
        val = index_queue.popleft()
        result[val] = attendee
        if index_queue:
            new_val = index_queue.popleft()
            index_queue.append(new_val)

    return result


# print(reveal_attendee_list_in_order([17, 13, 11, 2, 3, 5, 7]))
# print(reveal_attendee_list_in_order([1, 1000]))


# Problem 3: Arrange Event Attendees by Priority
"""This problem will provide an opportunity to modify the two pointers technique to solve a problem."""

# Understand
# What should we do when the priority does not exist in attendees list?
# Is it guaranteed that given input is always integers?
# What should we return when the given attendees list is empty?

# Plan
# Define three pointers, left, right and i pointing respectivelly at 0, len(attendees) -1, and 0.
# The logic is that we are moving all elements less than priority to left, and all elements greater than priority to the right, and the remaining element in the midddle.
# Loop through the given list attendees using the i pointer.
# if the current attendees is less than the specified priority, swap it with the attendees at the left position, and increment both left and i pointers by 1.
# if the current attendees is greater than the specified priority, swap it with the attendees at the right position, and decrement the right pointer by 1.
# If the current attendees is equal to the specified priority, just incremnt the i pointer by 1.
# Return the list of attendees

# Implement


def arrange_attendees_by_priority(attendees, priority):
    """Return the attendees list after the rearrangement."""
    n = len(attendees)-1
    left, i, right = 0, 0, n

    while i <= right:
        if attendees[i] < priority:
            attendees[left], attendees[i] = attendees[i], attendees[left]
            left += 1
            i += 1
        elif attendees[i] > priority:
            attendees[right], attendees[i] = attendees[i], attendees[right]
            right -= 1

        else:
            i += 1

    return attendees


print(arrange_attendees_by_priority([9, 12, 5, 10, 14, 3, 10], 10))
print(arrange_attendees_by_priority([-3, 4, 3, 2], 2))


# Standard Problem Set Version 2: Problem 5: Minimum Remaining Watchlist After Removing Movies
"""This problem will illustrate a greate understanding on how to use the stack data structure operation such as adding and removing. """
# Understand
# Is it guaranteed that the given string is always in alphabetic format?
# What should we return when the given string is empty?
# Is there a time or space complexity constraint?

# Plan
# Base case: Return 0, if length of given string is equal to 0.
# Declare a stack, initially empty, to store the final output letters.
# Loop through the watchlist string and do the following:
# if stack is not empty and current char is 'B' and top of stack is 'A', then remove top of stack.
# if stack is not empty and current char is 'C' and top of stack is 'D', then remove top of stack.
# Else: push current char into stack.
# Return len(stack)


# Implement
def min_remaining_watchlist(watchlist):
    """Return the minimum possible length of the modified watchlist that you can obtain."""
    if len(watchlist) == 0:
        return 0
    stack = []
    for char in watchlist:
        if stack and ((char == 'B' and stack[-1] == 'A') or (char == 'D' and stack[-1] == 'C')):
            stack.pop()
        else:
            stack.append(char)

    return len(stack)


print(min_remaining_watchlist("ABFCACDB"))
print(min_remaining_watchlist("ACBBD"))
