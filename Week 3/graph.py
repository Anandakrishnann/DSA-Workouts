class Graph:

    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print(f"Graph dictionary: {self.graph_dict}")


    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []
            print(f"Vertex {vertex} added")
        else:
            print(f"Vertex {vertex} already exists")


    def add_edge(self, start, end):
        if start in self.graph_dict:
            self.graph_dict[start].append(end)
        else:
            self.graph_dict[start] = [end]
            
        if end not in self.graph_dict:  
            self.graph_dict[end] = []
        
        print(f"Edge {start} -> {end} added")


    def get_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:  
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    
    def get_shortest_path(self, start, end):
        all_paths = self.get_paths(start, end)
        if not all_paths:
            return None
        shortest_path = min(all_paths, key=len)
        return shortest_path

    
    def has_path(self, start, end):
        return bool(self.get_paths(start, end))

    
    def display(self):
        print("Graph adjacency list:")
        for vertex in self.graph_dict:
            print(f"{vertex} -> {self.graph_dict[vertex]}")


if __name__ == "__main__":
    routes = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "D"),
        ("D", "E"),
        ("E", "F"),
        ("F", "G"),
    ]

    
    route_graph = Graph(routes)


    route_graph.add_edge('G', 'D')  
    route_graph.add_edge('H', 'D')  

    
    route_graph.display()

    
    start = "A"
    end = "D"
    print(f"All paths from {start} to {end}: {route_graph.get_paths(start, end)}")
    print(f"Shortest path from {start} to {end}: {route_graph.get_shortest_path(start, end)}")
