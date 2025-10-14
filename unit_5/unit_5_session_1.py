# Advanced Problem Set Version 1

# Problem 3: Group by Personality
"""I picked this problem because it demonstrate how to access attribute of a class in a function defined outside of that class."""
# Understand
# Is the constructor always given?
# What should we do when the list of townies is empty?
# What should we return when their is no match?
# Is there a time or space complexity constraint?

# Plan
# Declare a result variable to store the final output.
# Iterate over the townies list, append the name of the townie if townie.personality == personality_type.
# Otherwise, skip
# Return result list.
# Time complexity: best case is O(1) if townie contain only one element, worse case is O(n) where n is the number of townies.
# Space complexity: O(1) since we did not allocate any extra space.

# Implementation


class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
    # ... methods from previous problems


def of_personality_type(townies, personality_type):
    """Return the name that correspond to a given personality."""
    result = []
    for townie in townies:
        if townie.personality == personality_type:
            result.append(townie.name)
    return result


isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))
print(of_personality_type([isabelle, bob, stitches], "Normal"))


# Problem 4: Telephone
"""This problem emphasizes how to traverse a linked list. """
# Understand
# What should we do when the start_villager doesn't exist?
# What if the target_villager doesn't exist?
# The output format should always be a boolean variable?
# Is there a time or space complexity constraint?

# Plan
# Check for base case: return True if the start_villager's neighbor is the target_villager.
# while start_Villager exist, return true if start_villager's neighor equal to target_villager.
# Else, update start_villager to it current neighbor.
# If there is not match after existing the while loop, return False.

# Implement


class Villager_1:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor
    # ... methods from previous problems


def message_received(start_villager, target_villager):
    """that returns True if you can pass a message from the start_villager to the target_villager through a series of neighbors,
    and False otherwise."""
    if start_villager.neighbor == target_villager:
        return True
    while start_villager is not None:
        if start_villager == target_villager:
            return True
        else:
            start_villager = start_villager.neighbor
    return False


isabelle = Villager_1("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager_1("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager_1("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(message_received(isabelle, kk_slider))  # Output : True
print(message_received(kk_slider, isabelle))  # Output : False

# Problem 7: Fishing Probability
"""This problem demnstrates the use of both mathematical concept and how to travese a linked list."""
# Understand
# What should we do when the head of the linked list is Null?
# How about if a name of the fish is not present in the linked list?
# Do we need to take into account duplicate name?

# Plan
# Define a helper function to find the length of the linked list.
# Traverse the linked list and check if given fish name exist.
# If yes, then return 1/length_Of_linked_list.
# Otherwise, return 0.00
# Time complexity: best case is O(1) if LL contain only one element, worse case is O(n) where n is the length of linked list.
# Space complexity: O(1) since we did not allocate any extra space.
# Implement


class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing


def print_linked_list(head):
    """Print element in the list."""
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next


def find_length(head):
    """Return the number of elements in a linked list."""
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count


def fish_chances(head, fish_name):
    """Return the probability rounded down to the nearest hundredth that the player will catch a fish of type fish_name."""
    current = head
    while current:
        flag = False
        total_length = find_length(head)
        if current.fish_name == fish_name:
            flag = True
            break
        current = current.next
    if flag == True:
        return round((1/total_length), 2)
    else:
        return 0.00


fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))

print(fish_chances(fish_list, "Dace"))  # Output : 0.33
print(fish_chances(fish_list, "Rainbow Trout"))  # Output : 0.00
