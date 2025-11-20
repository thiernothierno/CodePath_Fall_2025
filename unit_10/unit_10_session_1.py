# Standard Set Version 1: Problem 1: Graphing Flights
# Understand
# What should we return when the graph is empty?
# Are we working with a directed or undirected graph?
# What should we return when have only one node in the graph?
# What should we do with disconnected graph with no edge?
# Is there a time or space complexity constrain?

# Plan
# Return False when there is flight.
# For each destination i, and for each destination j in flight[i], if i not in flight[j] then return False.
# Return True.
# Implement

def bidirectional_flights(flights):
    """Function that return True if for every fligh from destination i to j, then it also exist a fligh form destination j to i. False otherwise"""
    if not flights:
        return False
    n = len(flights)
    for i in range(n):
        for j in flights[i]:
            if i not in flights[j]:
                return False
    return True


flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))


# Problem 3: Finding Direct Flights
# Understand
# What should we return when there graph is empty?
# Is the source destination always greater than 0?
# What should we do when the source is greater than the size of the matrix?
# Is there a time or space complexity constrain?

# Plan
# Base case: Return an empty list when the matrix is empty or when the source is greater than the length of the matrix.
# Define an empty result list to store the final output?
# Iterate over the number of rows of the given matrix, and do the following:
# if flight[source][current_cell] equal to 1, then append current_cell to result.
# Return result.

# Implement
def get_direct_flights(flights, source):
    """Function that return a list of all destinations a customer can reach from source on a direct flight"""
    result = []
    if not flights or source > len(flights):
        return []
    for destination in range(len(flights)):
        if flights[source][destination] == 1:
            result.append(destination)

    return result


flights = [
    [0, 1, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0]]

print(get_direct_flights(flights, 2))
print(get_direct_flights(flights, 3))

# Problem 4: Converting Flight Representations
# Understand
# What should we return when the graph is empty?
# Are we working with a directed or undirected graph?
# What should we return when have only one node in the graph?
# What should we do with disconnected graph with no edge?
# Is there a time or space complexity constrain?

# Plan
# With this solution we assume that every flight has a source and a destination.
# IF not flights return []
# Define a output dictionary to store the final result.
# Let define a as the source and b the destination.
# Check if a is not in ouput, then create an entry. Otherwise add b as part of the values of a.
# Check if b is not in output, then create an entry. Otherwise add a as part of the values of b.
# Return output.

# Implement


def get_adj_dict(flights):
    """Function that return a dictionary where each key represent all source flight and values represent all destinations of the current key."""
    if not flights:
        return []
    output = {}
    for a, b in flights:
        if a not in output:
            output[a] = []
        output[a] += [b]

        if b not in output:
            output[b] = []
        output[b] += [a]
    return output


flights = [['Cape Town', 'Addis Ababa'], ['Cairo', 'Lagos'], ['Lagos', 'Addis Ababa'],
           ['Nairobi', 'Cairo'], ['Cairo', 'Cape Town']]
print(get_adj_dict(flights))
