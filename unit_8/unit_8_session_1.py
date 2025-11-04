
from collections import deque

# Advanced Problem Set Version 1: Problem 8: Twinning Trees
"""The reason I picked this problem is that it demonstrates how we can simultenuously traverse two trees at the same time."""
# Understand
# What should we return when both trees or one of the trees does not exist?
# What does identical trees means in this scenario?
# Is there a time or space complexity constraint?

# Plan
# Define an helper function, to check if trees are identical.
# Check for edge cases: Return True when both trees are empty.
# Return False when one of the tree is empty.
# Return false if value at both roots are not equal.
# Recursively call the helper function on the left subtree, and assign the result to a variable left.
# Recursively call the helper function on the right subtree, and assign the result to a variable right.
# Return left and right.
# Return the helper function passing root1, and root2 as argument.

# Implement


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def is_identical(root1, root2):
    """Function that return true if trees are identical, false otherwise."""
    def helper(node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        left = helper(node1.left, node2.left)
        right = helper(node1.right, node2.right)

        return left and right

    return helper(root1, root2)


root1 = TreeNode(1, TreeNode(2), TreeNode(3))
root2 = TreeNode(1, TreeNode(2), TreeNode(3))
root3 = TreeNode(1, TreeNode(2))
root4 = TreeNode(1, None, TreeNode(2))

print(is_identical(root1, root2))
print(is_identical(root3, root4))


# Advanced Problem Set Version 2: Problem 1: Escaping the Sea Caves
"""This problem emphasizes a partial traversal of a given tree, in this example only node on the left subtree of the root node."""
# Understand
# What should we do when tree is empty?
# What should we return when the tree has only right childs?
# How the resulting output should be?
# Does the order of returning left nodes matter?
# Is there a time or space complexity constraint?

# Plan
# Declare a result list to store the final output. Initially empty.
# Define a helper to do the work
# Check for edge cases: Return an empty list when root is empty.
# Append the root node inside result list.
# Recursively move down to left, and at each level append the node at left in result list.
# Call helper function on root node.
# Return result list.

# Implement


def leftmost_path1(root):
    """Function that return all nodes in the leftmost path (recursivelly)"""
    result = []

    def helper(node):
        if not node:
            return []
        result.append(node.val)
        if node.left:
            helper(node.left)
    helper(root)
    return result


system_a = TreeNode("CaveA",
                    TreeNode("CaveB", TreeNode("CaveD"), TreeNode("CaveE")),
                    TreeNode("CaveC", None, TreeNode("CaveF")))
system_b = TreeNode("CaveA", None, TreeNode("CaveB", None, TreeNode("CaveC")))

print(leftmost_path1(system_a))
print(leftmost_path1(system_b))

# Advanced Problem Set Version 2: Problem 2: Escaping the Sea Caves II (Iteratively)
"""I picked this problem because it demonstrates how we can combine different data structure to solve a problem."""
# Understand
# What should we do when tree is empty?
# What should we return when the tree has only right childs?
# How the resulting output should be?
# Does the order of returning left nodes matter?
# Is there a time or space complexity constraint?

# Plan
# Define a result list to store the final output. Initially empty.
# Check for edge cases: Return an empty list when the tree is empty.
# Declare a queue to help with the traversal.
# Append the root node into the queue.
# while queue is not empty, do the following:
# pop front element and append it to result list.
# IF left subtree exist, add it into the queue.
# Return result.

# Implement


def leftmost_path2(root):
    """Function that return all nodes in the leftmost path (Iteratively)"""
    if not root:
        return []
    result = []
    queue = deque()
    queue.append(root)
    while queue:
        curr_val = queue.popleft()
        if curr_val.left:
            queue.append(curr_val.left)
        result.append(curr_val.val)
    return result


system_a = TreeNode("CaveA",
                    TreeNode("CaveB", TreeNode("CaveD"), TreeNode("CaveE")),
                    TreeNode("CaveC", None, TreeNode("CaveF")))
system_b = TreeNode("CaveA", None, TreeNode("CaveB", None, TreeNode("CaveC")))

print(leftmost_path2(system_a))
print(leftmost_path2(system_b))
