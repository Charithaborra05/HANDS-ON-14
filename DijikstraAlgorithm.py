import heapq


def dijkstra_algorithm(graph, source):
    """
    Implementation of Dijkstra's algorithm to find the shortest paths
    from a single source in a non-negative weighted graph.
    
    Args:
        graph (dict): A dictionary representing the graph as adjacency lists. 
                      Each key is a vertex, and the value is a list of tuples (neighbor, weight).
        source (str): The starting vertex.

    Returns:
        tuple: A dictionary of shortest distances and a dictionary of predecessors.
    """
    # Priority queue to manage (cost, vertex)
    priority_queue = []
    heapq.heappush(priority_queue, (0, source))

    # Initialize distances and predecessors
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0
    predecessors = {vertex: None for vertex in graph}

    while priority_queue:
        current_cost, current_vertex = heapq.heappop(priority_queue)

        # Skip processing if the current cost is greater than the recorded shortest distance
        if current_cost > distances[current_vertex]:
            continue

        # Process neighboring vertices
        for neighbor, weight in graph[current_vertex]:
            new_cost = current_cost + weight

            # Update if a shorter path to the neighbor is found
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                predecessors[neighbor] = current_vertex
                heapq.heappush(priority_queue, (new_cost, neighbor))

    return distances, predecessors


def reconstruct_path(predecessors, target):
    """
    Reconstructs the shortest path to the target using the predecessors dictionary.

    Args:
        predecessors (dict): A dictionary mapping each vertex to its predecessor.
        target (str): The target vertex.

    Returns:
        list: The reconstructed path as a list of vertices.
    """
    path = []
    current = target
    while current is not None:
        path.insert(0, current)
        current = predecessors[current]
    return path


# Example graph definition
graph = {
    'A': [('B', 3), ('C', 5)],
    'B': [('C', 2), ('D', 6)],
    'C': [('B', 1), ('D', 4), ('E', 6)],
    'D': [('E', 2)],
    'E': [('A', 3), ('D', 7)],
}

# Run Dijkstra's algorithm from the source node 'A'
source = 'A'
distances, predecessors = dijkstra_algorithm(graph, source)

# Print the shortest distances
print(f"Shortest distances from source '{source}':")
for vertex, distance in distances.items():
    print(f"{vertex}: {distance}")

# Print the paths
print(f"\nShortest paths from source '{source}':")
for vertex in graph:
    path = reconstruct_path(predecessors, vertex)
    print(f"Path to {vertex}: {' -> '.join(path)}")
