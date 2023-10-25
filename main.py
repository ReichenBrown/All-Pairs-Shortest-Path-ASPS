import sys

def read_graph_file(file_name):
    graph = {}
    with open(file_name, 'r') as file:
        lines = file.readlines()

    for line in lines:
        elements = list(map(int, line.strip('{}').split(',')))
        start_vertex, end_vertex, weight = elements
        if start_vertex not in graph:
            graph[start_vertex] = {}
        graph[start_vertex][end_vertex] = weight

    return graph

def all_pairs_shortest_path(graph):
    vertices = set()
    for vertex in graph:
        vertices.add(vertex)
        for neighbor in graph[vertex]:
            vertices.add(neighbor)

    num_vertices = max(vertices)

    # Initialize the distance matrix with infinity
    dist = [[sys.maxsize] * (num_vertices + 1) for _ in range(num_vertices + 1)]

    # Initialize the diagonal elements with 0
    for vertex in vertices:
        dist[vertex][vertex] = 0

    # Fill the distance matrix based on graph data
    for vertex in graph:
        for neighbor in graph[vertex]:
            dist[vertex][neighbor] = graph[vertex][neighbor]

    # Floyd-Warshall algorithm
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

def find_shortest_path(distances, start_vertex, end_vertex):
    shortest_path = [start_vertex]
    current_vertex = start_vertex
    while current_vertex != end_vertex:
        next_vertex = min(
            [(neighbor, distances[current_vertex][neighbor]) for neighbor in range(1, len(distances[current_vertex]))],
            key=lambda x: x[1]
        )[0]
        shortest_path.append(next_vertex)
        current_vertex = next_vertex
    return shortest_path

def main():
    graph_file = 'graph.txt'
    graph = read_graph_file(graph_file)

    start_vertex = 1
    end_vertex = 5
    distances = all_pairs_shortest_path(graph)
    shortest_path = find_shortest_path(distances, start_vertex, end_vertex)

    if len(shortest_path) > 1:
        print(f"The shortest path from vertex {start_vertex} to {end_vertex} has length {distances[start_vertex][end_vertex]} "
              f"and looks like the following path: {shortest_path}")
    else:
        print(f"No path found from vertex {start_vertex} to {end_vertex}.")

if __name__ == "__main__":
    main()
