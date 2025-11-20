from collections import deque

# Standard Set Version1 : Problem 1: Can Rebook Flight
# Understand
# What should we return when the matrix is empty?
# What should we return when source equal to destination?
# Is there a time or space complexity constrain?

# Plan
# Use BFS traversal.
# Define a queue and add the source.
# Define a set to avoid visiting a node more than once.
# While queue is not empty, do the following:
# pop from element of the queue.
# Check for all neighbor of current cell, if their is a flight and neighbor is not yet visited.
# if neighbord is equal to destination, return True.
# Otherwise, add neighbord into queue and marke it as visited.
# If the queue is empty and we have not found the destination, return False.

# Implement


def can_rebook(flights, source, dest):
    queue = deque()
    visited = set()
    if source == dest:
        return
    queue.append(source)
    visited.add(source)

    while queue:
        edge = queue.popleft()
        for i in range(len(flights)):
            if flights[edge][i] == 1 and i not in visited:
                if i == dest:
                    return True
                queue.append(i)
                visited.add(i)

    return False


flights1 = [
    [0, 1, 0],  # Flight 0
    [0, 0, 1],  # Flight 1
    [0, 0, 0]  # Flight 2
]

flights2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# print(can_rebook(flights1, 0, 2))
# print(can_rebook(flights2, 0, 2))

# Problem 3: Number of Flights
# Understand
# What is the input and output of the function?
# Is there a time or space complexity that we should be aware of?
# What should we return when the input is empty?

# Plan
# Define a counter variable to keep track of the number of flights.
# We will use a queue to keep track of the current destination and a set to keep track of visited cell.
# Return True if source and destination are the same.
# Define an empty list visited to store the visited destinations.
# Inside the queue, pop the first element.
# For each neighbor of the current node,
# Check if their is a connection and if it is not visited.
# Return counter variable if the neighbor is equal to destination.
# If not, add it to the queue and mark it as visited.
# If the queue is empty and we have not found the destination, return -1.
# time complexity is O(N^2) where N is the number of nodes.
# space complexity is O(N).

# Implement


def counting_flights(flights, i, j):
    """Return the minimum number of flights needed to travel from airport i to airport j.
    If it is not possible to fly from airport i to airport j, return -1"""
    n = len(flights)
    if i == j:
        return 0

    queue = deque([i])
    visited = [False] * n
    visited[i] = True
    flights_count = 0

    while queue:
        flights_count += 1
        for _ in range(len(queue)):
            current = queue.popleft()

            for neighbor in range(n):
                if flights[current][neighbor] == 1 and not visited[neighbor]:
                    if neighbor == j:
                        return flights_count
                    queue.append(neighbor)
                    visited[neighbor] = True

    return -1


flights = [
    [0, 1, 1, 0, 0],  # Airport 0
    [0, 0, 1, 0, 0],  # Airport 1
    [0, 0, 0, 1, 0],  # Airport 2
    [0, 0, 0, 0, 1],  # Airport 3
    [0, 0, 0, 0, 0]  # Airport 4
]

# print(counting_flights(flights, 0, 2))
# print(counting_flights(flights, 0, 4))
# print(counting_flights(flights, 4, 0))

# Problem 1: Get Flight Cost
# Understand
# What should we return when the source is equal to destination?
# What should we do when the destination is not in the given flights?
# Do we need to return the route with the less cost?
# Is there a time or space complexity constrain?

# Plan
# Declare a set to keep track visited cell.
# Define a variable to keep track the cost of visited cell.
# Use a helper function for dfs with backtracking.
# if current cell equal to destination, return cost.
# Othewise, mark current cell as visited.
# Go through all neighbord of current cell and do the following:
# IF neighbord not visited, recursively calculate the cost.
# IF valid path found, return result
# Unmark the current cell as visited.
# Return -1, if path not found.

# Implement


def calculate_cost(flights, start, dest):
    visited = set()

    def dfs(current, total_cost):
        if current == dest:
            return total_cost

        # Mark the current node as visited
        visited.add(current)

        for neighbor, cost in flights.get(current, []):
            if neighbor not in visited:
                result = dfs(neighbor, total_cost + cost)
                if result != -1:
                    return result
        visited.remove(current)

        return -1
    return dfs(start, 0)


flights = {
    'LAX': [('SFO', 50)],
    'SFO': [('LAX', 50), ('ORD', 100), ('ERW', 210)],
    'ERW': [('SFO', 210), ('ORD', 300)],
    'ORD': [('ERW', 300), ('SFO', 100), ('MIA', 400)],
    'MIA': [('ORD', 400)]
}

print(calculate_cost(flights, 'LAX', 'MIA'))
