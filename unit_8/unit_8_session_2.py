from collections import deque

# Advance Problem set Version 1: Problem 1: Sorting Plants by Rarity
"""This problem emphasizes one way of tree traversal: Inorder traversal (left-root-right). """
# Understand
# Is it guaranteed that the given tree will always be a BST?
# What should we do when the tree is empty?
# How the output should look like?
# Is there a time or space complexity constraint?
# Plan
# Define an empty result list to store the final output.
# Check for edge case: Return [] when the tree is empty.
# Use Inorder traversal to traverse the tree. (left-root-right) since we are dealing with a BST.
#
# Implement


class TreeNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key      # Plant rarity
        self.val = val      # Plant name
        self.left = left
        self.right = right


def sort_plants(collection):
    """Function that return a sorted array of plant nodes as tuple (key, value) from least to more rare"""
    result = []

    def inorder_traversal(root):
        if not root:
            return
        inorder_traversal(root.left)
        result.append((root.key, root.val))
        inorder_traversal(root.right)
    inorder_traversal(collection)
    return result


node = TreeNode(3, "Monstera")
node.left = TreeNode(1, "Pothos")
node.left.right = TreeNode(2, "Spider Plant")
node.right = TreeNode(5, "Witchcraft Orchid")
node.right.left = TreeNode(4, "Hoya Motoskei")


print(sort_plants(node))

# Advance Problem Set Version 2: Problem 1: Sorting Pearls by Size
"""This problem demonstrates how we can implement inorder traversal iteratively using a stack."""
# Understand
# Is it guaranteed that the given tree will always be a BST?
# What should we do when the tree is empty?
# How the output should look like?
# Is there a time or space complexity constraint?

# Plan
# Define a result list to store the final output.
# Declare a stack to keep track visited element.
# while stack or root, do the following:
# while root, append root to stack, and move root to the left subtree.
# Pop top element from stack, and store it value in result list.
# Now point root to the right subtree.
# Return result list.

# Implement


def smallest_to_largest_iteratively(pearls):
    if not pearls:
        return []
    sorted_list = []
    stack = []
    current = pearls
    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        top_val = stack.pop()
        sorted_list.append((top_val.key, top_val.val))
        current = top_val.right

    return sorted_list


print(smallest_to_largest_iteratively(node))

# Problem 2: Searching Ariel's Treasures
"""This problem demonstrates how we can use any tree traversal(preorder, inorder, postorder) to check if given node exist in a tree. """
# Understand
# What should we do when the tree is empty?
# How the output format should look like?
# Is there a time or space complexity constraint?

# Plan
# Check for edge cases: Return false when tree is empty.
# Use preorder traversal:
# start from the root, return true if root is same as given input.
# Recursively check the left subtree.
# Recursively check the right subtree.
# IF input not found, return False
# Implement


class TreeNode1():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def locate_treasure(grotto, treasure):
    """Function that return true if if given node exist in tree, false otherwise."""
    if not grotto:
        return False
    if grotto.val == treasure:
        return True
    left = locate_treasure(grotto.left, treasure)
    right = locate_treasure(grotto.right, treasure)
    return left or right


system_a = TreeNode1("CaveA",
                     TreeNode1("CaveB", TreeNode1(
                         "CaveD"), TreeNode1("CaveE")),
                     TreeNode1("CaveC", None, TreeNode1("CaveF")))
system_b = TreeNode1("CaveA",
                     TreeNode1("CaveB", TreeNode1(
                         "CaveD"), TreeNode1("CaveE")),
                     TreeNode1("CaveC", None, TreeNode1("CaveF")))

print(locate_treasure(system_a, "CaveE"))
print(locate_treasure(system_b, "CaveM"))
