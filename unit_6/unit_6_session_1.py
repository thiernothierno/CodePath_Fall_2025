
# Standard Problem Set Version 1
# Problem 6: Volume Control
"""I picked this problem because it demonstrates a great manipulation of pointers."""
# Understand
# What should we return when the head of the given linked list is empty?
# What about if the linked list has only one element?
# Is there a time or space complexity constraint?

# Plan
# Define a counter variable to store the output result. Initially count = 0
# Check for edge cases: return none if head is none and return 0 if head.next is none
# Declare a pointer previous which will point to head.
# Declare another pointer current for linked list traversal, which will initially point to head.next.
# Loop through the linked list using the current pointer.
# while curr.next, declare another pointer forward which will point to curr.next.
# If minima and maxima is satisfied, increment the count variable by 1.
# Update pointers: prev = curr and curr = curr.next
# Return count
# Time complexity: O(n) as we need to traverse the entire linked list, where n is number of elements.
# Space Complexity: O(1) as we are only declaring varibles to store value or addresses.

# Implement


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing


def print_linked_list(head):
    """Function that display elements of a linked list."""
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next


def count_critical_points(song_audio):
    """Function that return the total number of critical point."""
    if not song_audio:
        return None
    if not song_audio.next:
        return 0
    count = 0
    prev = song_audio
    curr = song_audio.next
    while curr.next:
        forward = curr.next
        if (curr.value < prev.value and curr.value < forward.value) or (curr.value > prev.value and curr.value > forward.value):
            count += 1

        prev = curr
        curr = curr.next
    return count


song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))

# print(count_critical_points(song_audio))


# Standart Set Vertion 2
# Problem 2: 200 Points for Gryffindor
"""This problem emphasizes how we can combine different data structures to solve a problem such as dictionary + linked list."""
# Understand
# What should we do when the linked list is empty?
# What should we return when the given score doesn't exist?
# Is there a time or space complexity constraint?

# Plan
# Return 0 if the linked list is empty?
# Declare a dictionary to store value as key and their frequency as their total count.
# Declare a pointer curr which will point to the head of the linked list.
# Iterate over the linked using the curr pointer.
# If current value exist in dictionary, then increment it frequency by 1
# Otherwise, set it frequency to 1.
# Loop through the dictionary, return value if key == score.
# Time complexity: O(n) since we need to scan each node in the linked list.
# Space complexity: O(n) since we declare a dictionary to store data.

# Implement


class Node1:
    def __init__(self, house, score, next=None):
        self.house = house
        self.value = score
        self.next = next


def count_element(house_points, score):
    if not house_points:
        return 0
    curr = house_points
    my_dictionary = {}
    while curr:
        if curr.value in my_dictionary:
            my_dictionary[curr.value] += 1
        else:
            my_dictionary[curr.value] = 1
        curr = curr.next
    for key, value in my_dictionary.items():
        if score == key:
            return value


house_points = Node1("Gryffindor", 600,
                     Node1("Ravenclaw", 300,
                           Node1("Slytherin", 500,
                                 Node1("Hufflepuff", 600))))

# print(count_element(house_points, 600))

# Advance Set Version 1
# Problem 2: Protein Folding Loop Detection
"""This problem demonstrate the use of the Hare and tortoise technique"""
# Understand
# Is an empty linked list considered as a cycle?
# What should we return when length of linked list is 1?
# Is there a time or space complexity constraint?

# Plan
# Declare a result empty array to store the output values.
# Declare two pointers slow and fast to check if the linked list has a cycle.
# Move slow pointer by one step, and fast pointer by two steps.
# If slow and fast pointers point to the same node, this mean there is a cycle.
# Otherwise, there is not cycle return an empty list.
# Now, we need to find the begining of the cycle, by reassigning slow pointer to the head of the linked list.
# While slow != fast, move both of them with the same speed, one step.
# Assign another pointer to where slow and fast meet, which is the beginning of the cycle.
# Collect nodes in the cycle.
# Return result list.
# Time complexity: O(n) since we need to scan each node in the linked list.
# Space complexity: O(n) since we declare a list to store data.

# Implement


def cycle_length(protein):
    """Function that return all elements present in a cycle."""
    result = []
    slow = protein
    fast = protein
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return []

    slow = protein
    while slow != fast:
        slow = slow.next
        fast = fast.next

    begining_of_cycle = slow
    while True:
        result.append(slow.value)
        slow = slow.next
        if slow == begining_of_cycle:
            break

    return result


protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
protein_head.next.next.next.next = protein_head.next
print(cycle_length(protein_head))
