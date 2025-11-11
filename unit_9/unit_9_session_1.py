from collections import deque

# Advance Problem set version1: Problem 1: Croquembouche II
"""The reason I picked this problem is because it demonstrates another traversal method called BFS which is also widely used in solving Tree related problems."""
# Understand
# How the ouptut format should be?
# What should we return when the tree is empty?
# What traversal do we need to be focus on? DFS or BFS?
# Are we allowed to use another data structure to solve the problem?
# Is there a time or space complexity constraint?

# Plan
# Return [], when the tree is empty.
# Use BFS to traverse the tree.
# Define an output list to store the final result.
# Add the root node into the queue.
# While queue is not empty, do the following:
# Define a result list to store element by level.
# store the length of the queue in a variable n.
# Iterate over the n, and do the following:
# pop element in front from the queue, and store it into a variable node.
# Append node.val into the result list.
# If node.left exist, append it into the queue.
# If node.right exist, append it into the queue.
# Outside the for loop, append result list into output list.
# Outside the while loop, return output list.
# Time complexity: O(n) since we need to visite each node in the tree, and n is the heigh of tree.
# Space complexity: O(n) since we need to declare two lists to store our data.

# Implement


class Puff():
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right


def listify_design(design):
    """Function that return element of a tree by level"""
    if not design:
        return []

    queue = deque([design])
    output = []
    while queue:
        n = len(queue)
        result = []
        for i in range(n):
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        output.append(result)
    return output


croquembouche = Puff("Vanilla",
                     Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")),
                     Puff("Strawberry"))
print(listify_design(croquembouche))


# Problem 2: Icing Cupcakes in Zigzag Order
# Understand
# How the ouptut format should be?
# What should we return when the tree is empty?
# What traversal do we need to be focus on? DFS or BFS?
# Are we allowed to use another data structure to solve the problem?
# Is there a time or space complexity constraint?

# Plan
# Return [], when the tree is empty.
# Use BFS to traverse the tree.
# Define an output list to store the final result.
# Add the root node into the queue.
# While queue is not empty, do the following:
# pop element in front from the queue, and store it into a variable node.
# Append node.val into the result list.
# If node.left exist, append it into the queue.
# If node.right exist, append it into the queue.
# Outside the while loop, return output list.
# Time complexity: O(n) since we need to visite each node in the tree, and n is the heigh of tree.
# Space complexity: O(n) since we need to declare a list to store our data.

# Implement
def zigzag_icing_order(cupcakes):
    """Function that return element of a tree in a zigzig format"""
    if not cupcakes:
        return []
    queue = deque([cupcakes])
    output = []
    while queue:
        node = queue.popleft()
        output.append(node.val)
        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)
    return output


croquembouche = Puff("Vanilla",
                     Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")),
                     Puff("Strawberry"))
print(zigzag_icing_order(croquembouche))

# Problem 3: Larger Order Tree
# Understand
# How the ouptut format should be?
# What should we return when the tree is empty?
# What traversal do we need to be focus on? DFS or BFS?
# Are we allowed to use another data structure to solve the problem?
# Is there a time or space complexity constraint?

# Plan
# Check for edge cases: Return None, when the tree is empty.
# Define a helper function that takes a node and cummulative_sum, then implement a postorder traversal (right-root-left).
# Call the helper functon on the right subtree.
# Update cummulative_sum
# Call the helper function on the left subtree.

# Implement


class TreeNode():
    def __init__(self, order_size, left=None, right=None):
        self.val = order_size
        self.left = left
        self.right = right


def print_tree(root):
    """Function that print value of a tree"""
    if not root:
        return None
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)


def larger_order_tree(orders):
    """Function that return the number of cupcakes a custormer ordered"""
    def helper(root, cum_sum):
        if not root:
            return cum_sum

        cum_sum = helper(root.right, cum_sum)
        root.val += cum_sum
        cum_sum = root.val

        return helper(root.left, cum_sum)

    helper(orders, 0)
    return orders


node = TreeNode(4)
node.left = TreeNode(1)
node.right = TreeNode(6)
node.left.left = TreeNode(0)
node.left.right = TreeNode(2)
node.right.left = TreeNode(5)
node.right.right = TreeNode(7)
node.left.right.right = TreeNode(3)
node.right.right.right = TreeNode(8)
print_tree(larger_order_tree(node))
