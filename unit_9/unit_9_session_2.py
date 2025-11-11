# Advance Problem Set Version 1:  Problem 1: Creating Cookie Orders from Descriptions

# Understand
# What should we do when their is no element in description?
# How the output format should look like?
# Is there a time or space complexity constraint?

# Plan
# Define a dictionary that will help buil a parent-child relationship. dictionary = {}
# Define a set to keep track all visited child. my_set = set()
# Iterate over the given description, and do the following:
# 1- if parent not in dictionary, create a node with parent as it value.
# 2- If child not in dictionary, create a node with child as it value.
# 3- Add child into my_set.
# 4- check if is_left is equal to 1, dictionary[parent].left = dictionary[child]
# 5- Else: dictionary[parent].right = dictionary[child]
# Repeat step 1-5.
# Declare a variable root, which initially equal to None, to find the root of the tree.
# Iterate over the dictionary, and if we found an element is not present in my_set, assign it as root.
# root = dictionary[parent]
# Return root.

# Implement
class TreeNode:
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right


def print_tree(root):
    """Function that print value of a tree"""
    if not root:
        return None
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)


def build_cookie_tree(descriptions):
    """Function that build a tree based on a given rules."""
    dictionary = {}
    my_set = set()

    for parent, child, is_left in descriptions:
        if parent not in dictionary:
            dictionary[parent] = TreeNode(parent)
        if child not in dictionary:
            dictionary[child] = TreeNode(child)
        my_set.add(child)

        if is_left == 1:
            dictionary[parent].left = dictionary[child]
        else:
            dictionary[parent].right = dictionary[child]

    root = None
    for parent in dictionary:
        if parent not in my_set:
            root = dictionary[parent]
            break

    return root


descriptions1 = [
    ["Chocolate Chip", "Peanut Butter", 1],
    ["Chocolate Chip", "Oatmeal Raisin", 0],
    ["Peanut Butter", "Sugar", 1]
]

descriptions2 = [
    ["Ginger Snap", "Snickerdoodle", 0],
    ["Ginger Snap", "Shortbread", 1]
]

# Using print_tree() function included at top of page
print_tree(build_cookie_tree(descriptions1))
# print_tree(build_cookie_tree(descriptions2))

# Problem 2: Cookie Sum
# Understand
# What should we return when the tree is empty?
# Does the values in the tree are all integers?
# Is there a time or space complexity constraint?

# Plan
# Use a dfs to traverse the tree.
# Define a helper function,
# Implement


def count_cookie_paths(root, target_sum):
    """Function that return the total number of unique path from root to leaf."""
    if not root:
        return 0

    def helper(node, curr_sum):
        if not node:
            return 0

        curr_sum += node.val

        if node.left is None and node.right is None:
            if curr_sum == target_sum:
                return 1
            else:
                return 0

        left = helper(node.left, curr_sum)
        right = helper(node.right, curr_sum)
        return left + right

    return helper(root, 0)


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(8)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(4)

print(count_cookie_paths(root, 22))

# Understand
# Plan
# Implement
