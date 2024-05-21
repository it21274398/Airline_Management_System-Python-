from graph import Graph, bfs, display_routes
from hash_table import HashTable
from heap_sort import sort_routes

def main():
    # Create and populate the graph
    graph = Graph()
    print("Enter graph edges (source destination distance):")
    print("Example input: A B 100")
    print("Type 'done' when finished.")
    while True:
        edge = input().split()
        if edge[0] == 'done':
            break
        graph.add_edge(edge[0], edge[1], int(edge[2]))

    # Create and populate the hash table
    hash_table = HashTable(10)
    print("\nEnter hash table data (key value):")
    print("Example input: JFK John F. Kennedy International Airport")
    print("Type 'done' when finished.")
    while True:
        data = input().split()
        if data[0] == 'done':
            break
        hash_table.insert(data[0], ' '.join(data[1:]))

    # Test data for Heap Sort
    routes = []
    print("\nEnter routes (path distance):")
    print("Example input: A,B,D 200")
    print("Type 'done' when finished.")
    while True:
        route = input().split()
        if route[0] == 'done':
            break
        routes.append((route[0].split(','), int(route[1])))

    # Perform BFS to find routes
    print("\nFinding routes using BFS:")
    source = input("Enter source node: ")
    destination = input("Enter destination node: ")
    max_depth = int(input("Enter maximum depth: "))
    routes = bfs(graph, source, destination, max_depth)
    display_routes(routes)

    # Sort routes by distance
    sorted_by_distance = sort_routes(routes, 'distance')
    print("\nRoutes sorted by distance:")
    display_routes(sorted_by_distance)

    # Sort routes by layovers
    sorted_by_layovers = sort_routes(routes, 'layovers')
    print("\nRoutes sorted by layovers:")
    display_routes(sorted_by_layovers)

if __name__ == "__main__":
    main()
