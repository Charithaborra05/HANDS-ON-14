def bellman_ford_algorithm(graph, source):
    """
    Implementation of the Bellman-Ford algorithm to find the shortest paths
    from a single source in a weighted graph. Handles negative weights.
    
    Args:
        graph (dict): A dictionary representing the graph as adjacency lists. 
                      Each key is a vertex, and the value is a list of tuples (neighbor, weight).
        source (str): The starting vertex.

    Returns:
        tuple: A dictionary of shortest distances and a dictionary of predecessors.
        
    Raises:
        ValueError: If the graph contains a negative weight cycle.
    """
    # Initialize distances and predecessors
    distances = {vertex: float('inf') for vertex in graph}
    predecessors = {vertex: None for vertex in graph}
    distances[source] = 0

    # Extract edges from the graph
    edges = [(start, end, weight) for start in graph for end, weight in graph[start]]

    # Relax edges |V| - 1 times
    for _ in range(len(graph) - 1):
        for start, end, weight in edges:
            if distances[start] + weight < distances[end]:
                distances[end] = distances[start] + weight
                predecessors[end] = start

    # Check for negative weight cycles
    for start, end, weight in edges:
        if distances[start] + weight < distances[end]:
            raise ValueError("The graph contains a negative weight cycle.")

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


# Example graph structure
graph = {
    'A': [('B', 3), ('C', 5)],
    'B': [('C', 2), ('D', 6)],
    'C': [('B', 1), ('D', 4), ('E', 6)],
    'D': [('E', 2)],
    'E': [('A', 3), ('D', 7)],
}

# Run the Bellman-Ford algorithm from the source node 'A'
try:
    source = 'A'
    distances, predecessors = bellman_ford_algorithm(graph, source)

    print(f"Minimum distances from source '{source}':")
    for vertex, distance in distances.items():
        print(f"{vertex}: {distance}")

    print("\nShortest paths from source:")
    for vertex in graph:
        path = reconstruct_path(predecessors, vertex)
        print(f"Path to {vertex}: {' -> '.join(path)}")
except ValueError as error:
    print(error)
