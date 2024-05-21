from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, src, dest, distance):
        if src not in self.adj_list:
            self.adj_list[src] = []
        self.adj_list[src].append((dest, distance))

def bfs(graph, start, goal, max_layovers):
    queue = deque([(start, [start], 0)])  # (current airport, path, distance)
    routes = []
    
    while queue:
        current, path, distance = queue.popleft()
        if len(path) - 1 > max_layovers:
            continue
        
        for neighbor, dist in graph.adj_list.get(current, []):
            if neighbor == goal:
                routes.append((path + [neighbor], distance + dist))
            else:
                queue.append((neighbor, path + [neighbor], distance + dist))
    
    return routes

def display_routes(routes):
    for route in routes:
        path, distance = route
        print(f"Route: {' -> '.join(path)}, Layovers: {len(path) - 2}, Distance: {distance} km")

# Example usage:
graph = Graph()
graph.add_edge('A', 'B', 100)
graph.add_edge('A', 'C', 200)
graph.add_edge('B', 'C', 150)
graph.add_edge('C', 'D', 100)

routes = bfs(graph, 'A', 'D', 2)
display_routes(routes)
