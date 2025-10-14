# Advanced Problem Set Version 1

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

# For testing


def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next


# Problem 2: Remove Tail
"""This problems shows how to traverse, move and update pointers in a linked list."""
# Error: The reason why this code is not working as it suppose to, is because we are iterating the entire linked list and after the while loop we are pointing back to the end of the last node. Therefore, it return the entire linked list without deleting the last node.
# Solution: Declare a tmp pointer that will point the node before the current node while traversing the linked list.
# As we traverse the linked list, when we reach the end of the linked list, delete the last pointer by pointing tmp pointer to Null.
# Return head of the linked list.

# Implement


def remove_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None

    current = head
    while current.next:
        tmp = current
        current = current.next
    tmp.next = None
    # current.next = None

    return head


head = Node("Isabelle", Node("Alfonso", Node("Cyd")))

# Linked List: Isabelle -> Alfonso -> Cyd
print_linked_list(remove_tail(head))


# 1 - > 2 - > 3 -> 4 -> 5


# Problem 3: Delete Duplicates in a Linked List
"""This problems emphasizes different techniques use in a sorted linked list such as defining, moving, updating, and removing pointers."""
# Understand
# Is the linked list always sorted?
# What should we do when the linked list is not sorted?
# The output format should be a linked list?
#
# Plan
# Define a tmp node, and point tmp.next to head.
# Declare another variable prev that will point to tmp.
# Have another variable current that will point to head.
# Check for base cases: 1- return None when the linked list is empty. 2- return head when head.next is null.
# Iterate over the linked list and do the following:
# Move the current variable to next node when both values of current and current.next are equal.
# Move prev to next node if prev.next equal to current.
# Otherwise, skip all duplicate value by pointing prev.next to current.next
# At the end move current pointer to next node.
# Time complexity: O(n), since we need to scan each node once ( n is the number of nodes in the Linked list ).
# Space complexity: O(1), since we are not using any extra space. We are only declaring few pointers to update link.
# Implement


def delete_dupes(head):
    """delete all elements that occur more than once in the list (not just the duplicates).
      The resulting list should maintain sorted order."""
    if head is None:
        return None
    if head.next is None:
        return head

    tmp = Node(0)
    tmp.next = head
    prev = tmp
    current = head

    while current:
        while current.next and current.value == current.next.value:
            current = current.next

        if prev.next == current:
            prev = prev.next
        else:
            prev.next = current.next

        current = current.next

    return tmp.next


head_1 = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))
head_2 = Node(1, Node(2, Node(2, Node(2, Node(3, Node(3, Node(3)))))))

print_linked_list(delete_dupes(head_1))  # Output : 1 -> 2 -> 4 -> 5
print_linked_list(delete_dupes(head_2))  # Output : 1


# Problem 4: Does it Cycle?
"""This problem demonstrates how to use the Hare and Tortoise technique to check if a linked list is cyclique or not."""
# Understand
# What does it mean for a linked list to have a cycle?
# Does only one node in a linked list means that cycle exist?
# Does the linked list contain duplicate element?


# Plan
# Check for base case: return false when the linked list is either Null or contain only one node.
# Declare two pointers slow and fast.
# Point both pointers to the head of the linked list.
# Traverse the linked list and move slow pointer to one step, and fast to two step.
# Return true, if slow and fast pointers point to the same node.
# Return false if we reach the end of the linked list, and a cycle is not detected.
# Time complexity: O(n), since we need to scan each node once ( n is the number of nodes in the Linked list ).
# Space complexity: O(1), since we are not using any extra space. We are only declaring few pointers to update link.

# Implement
def has_cycle(head):
    """Returns True if the list has a cycle in it and False otherwise."""
    slow = head
    fast = head

    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False


peach = Node("Peach", Node("Luigi", Node("Mario", Node("Toad"))))

# Toad.next = Luigi
peach.next.next.next = peach.next

print(has_cycle(peach))
