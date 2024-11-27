def floyd_warshall_algorithm(graph):
    """
    Floyd-Warshall algorithm to compute shortest paths between all pairs of vertices.
    
    Args:
        graph (dict): A dictionary where each key is a vertex, and its value is a list of tuples
                      representing edges as (neighbor, weight).

    Returns:
        tuple: 
            - A 2D list representing the shortest distances between each pair of vertices.
            - A 2D list representing the next vertices on the shortest paths.
            - A list of vertices corresponding to indices in the matrices.
    """
    # Extract all vertices and map them to indices
    vertices = list(graph.keys())
    vertex_indices = {vertex: index for index, vertex in enumerate(vertices)}
    num_vertices = len(vertices)

    # Initialize distance and path matrices
    distances = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    next_vertex = [[None] * num_vertices for _ in range(num_vertices)]

    # Set distance from each vertex to itself as zero
    for i in range(num_vertices):
        distances[i][i] = 0

    # Populate initial distances based on edges in the graph
    for origin in graph:
        for destination, weight in graph[origin]:
            i, j = vertex_indices[origin], vertex_indices[destination]
            distances[i][j] = weight
            next_vertex[i][j] = destination

    # Perform Floyd-Warshall updates
    for k in range(num_vertices):  # Intermediary vertex
        for i in range(num_vertices):  # Source vertex
            for j in range(num_vertices):  # Destination vertex
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
                    next_vertex[i][j] = next_vertex[i][k]

    return distances, next_vertex, vertices


def display_matrix(matrix, vertices, title="Matrix"):
    """
    Displays a 2D matrix in a human-readable format.
    
    Args:
        matrix (list): 2D list of values (distances or paths).
        vertices (list): List of vertex labels.
        title (str): Title for the matrix display.
    """
    print(f"\n{title}:")
    print("    ", "  ".join(vertices))
    for i, row in enumerate(matrix):
        print(f"{vertices[i]:<4}", "  ".join(f"{val if val != float('inf') else '∞':<4}" for val in row))


def reconstruct_path(next_vertex, vertices, start, end):
    """
    Reconstructs the shortest path from start to end using the next_vertex matrix.
    
    Args:
        next_vertex (list): 2D list where next_vertex[i][j] gives the next vertex to visit.
        vertices (list): List of vertex labels.
        start (str): Start vertex.
        end (str): End vertex.

    Returns:
        list: A list of vertices representing the shortest path.
    """
    vertex_indices = {vertex: index for index, vertex in enumerate(vertices)}
    i, j = vertex_indices[start], vertex_indices[end]

    if next_vertex[i][j] is None:
        return []  # No path exists

    path = [start]
    while start != end:
        start = next_vertex[i][j]
        path.append(start)
        i = vertex_indices[start]

    return path


# Graph representation as an adjacency list
graph = {
    'A': [('B', 3), ('C', 5)],
    'B': [('C', 2), ('D', 6)],
    'C': [('B', 1), ('D', 4), ('E', 6)],
    'D': [('E', 2)],
    'E': [('A', 3), ('D', 7)],
}

# Execute the Floyd-Warshall algorithm
distances, next_vertex, vertices = floyd_warshall_algorithm(graph)

# Display the shortest path distance matrix
display_matrix(distances, vertices, title="Shortest Path Distance Matrix")

# Reconstruct and display paths between specific pairs
print("\nShortest paths between vertices:")
for start in vertices:
    for end in vertices:
        if start != end:
            path = reconstruct_path(next_vertex, vertices, start, end)
            path_str = " -> ".join(path) if path else "No path"
            print(f"Path from {start} to {end}: {path_str}")
