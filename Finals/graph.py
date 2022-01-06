from vertex import Vertex


class Graph:
    def __init__(self):
        self.vertices_dictionary = {}
        self.number_of_vertices = 0

    def add_edge(self, src, dest):
        if src not in self.vertices_dictionary.keys():
            self.vertices_dictionary[src] = Vertex(src)
        if dest not in self.vertices_dictionary.keys():
            self.vertices_dictionary[dest] = Vertex(dest)
        self.vertices_dictionary[src].add_neighbor(dest)


