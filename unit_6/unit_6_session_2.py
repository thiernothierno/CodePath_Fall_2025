# Problem Set Version 1
# Problem 1: Wild Goose Chase
"""This problem demonstrate the slow and fast pointers technique also known as the Hare and Tortoise technique"""


# Understand
# WHat should we return when the linked list is empty?
# What should we return when the linked list contain only one element?
# Is there a time or space complexity constraint?

# Plan
# Check for edge cases: Return False if not head and head.next
# Declare two pointers slow and fast which will move simultaneously at one step and two steps respectively.
# While fast and fast.next
# IF slow pointer is equal to fast pointer, then return True
# Move slow pointer 1 step ahead and fast pointer two steps ahead.
# Return False, if not cycle found.
# Time Complexity: O(N)
# Space Complexity: O(1

# Implement
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_circular(clues):
    """Function that return True if there is a cycle, False otherwise."""
    if not clues or not clues.next:
        return False
    slow = clues
    fast = clues.next
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False


# Example 1
clue1 = Node("The stolen goods are at an abandoned warehouse")
clue2 = Node("The mayor is accepting bribes")
clue3 = Node("They dumped their disguise in the lake")
clue4 = Node("Another node")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue2

# Example 2:
clue5 = Node("The stolen goods are at an abandoned warehouse")
clue6 = Node("The mayor is accepting bribes")
clue7 = Node("They dumped their disguise in the lake")
clue8 = Node("Another node")
clue5.next = clue6
clue6.next = clue7
clue7.next = clue8
clue8.next = None

clue9 = Node("a")
clue10 = Node(None)
clue9.next = clue9
print(is_circular(clue9))
print(is_circular(clue1))
print(is_circular(clue5))


# Problem 1: Wild Goose Chase
"""This problem emphasizes a combination of the Hare and Tortoise technique as well how we can track all nodes present in a cycle."""

# Understand
# WHat should we return when the linked list is empty?
# What should we return when the linked list contain only one element?
# What should we return when there is not cycle in the linked list?
# Is there a time or space complexity constraint?

# Plan
# Declare an empty list result to store the output.
# Check for edge cases: Return [] if not head and head.next
# Declare two pointers slow and fast which will move simultaneously at one step and two steps respectively.
# While fast and fast.next
# IF slow pointer is equal to fast pointer, declare a new pointer meet that will point to either fast or slow and break the loop.
# Else: Move slow pointer 1 step ahead and fast pointer two steps ahead.
# Declare another pointer start which will point to the meet pointer.
# While start:
# Append current value to result list.
# Move start one step ahead.
# If start is equal to meet, exit the loop.
# Return result list.

# Time Complexity: O(N)
# Space Complexity: O(1)

# Implement


def collect_false_evidence(evidence):
    """Function that return all node in a cycle if there is a cycle."""
    if not evidence or not evidence.next:
        return []
    result = []
    slow = evidence
    fast = evidence.next
    meet = None
    while fast and fast.next:
        if slow == fast:
            meet = slow
            break
        slow = slow.next
        fast = fast.next.next

    start = meet
    while start:
        result.append(start.value)
        start = start.next
        if start == meet:
            break
    return result


# Example 1
clue1 = Node("A")
clue2 = Node("B")
clue3 = Node("C")
clue4 = Node("D")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2
# Example 2
clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")
clue5.next = clue6
clue6.next = clue7
clue7.next = None

print(collect_false_evidence(clue1))
print(collect_false_evidence(clue5))

# Problem 3: Prioritizing Suspects
"""This problem demonstrates the manipulation of pointers from one node to another."""
# Understand
# WHat should we return when the linked list is empty?
# What should we return when the linked list contain only one element?
# How the element should we return? In order as they appear in the original list?
# Is there a time or space complexity constraint?

# Plan
# Create two new nodes, greater_than and lesser_than, initially empty.
# Declare two pointers, greater and lesser pointing to the newly created Nodes respectively.
# Declare another pointer curr pointing to the head of the linked list.
# While curr:
# if curr.value > threshold, then point lesser pointer to curr pointer, and move lesser one step ahead
# Else: point greater to curr pointer, and move greater one step ahead.
# Move curr pointer one step ahead.
# After the while loop, point greater pointer to lesser_than and lesser pointer to None
# Return greater_than if greater-than.next is equal to None
# Else, return lesser_than.next

# Implement
# For testing


def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next


def partition(suspect_ratings, threshold):
    """Function that return all elements greater than or equal to threshold in front, and elements less than threshold in the back. """
    if not suspect_ratings:
        return None
    if not suspect_ratings.next:
        return suspect_ratings

    greater_than_threshold = Node(0)
    less_than_threshold = Node(0)

    greater = greater_than_threshold
    lesser = less_than_threshold
    current = suspect_ratings
    while current:
        if current.value < threshold:
            lesser.next = current
            lesser = lesser.next
        else:
            greater.next = current
            greater = greater.next
        current = current.next
    greater.next = less_than_threshold.next
    lesser.next = None

    if greater_than_threshold.next:
        return greater_than_threshold.next
    else:
        return less_than_threshold.next


suspect_ratings = Node(7, Node(1, Node(5, Node(2, Node(9, Node(2))))))

print_linked_list(partition(suspect_ratings, 3))
