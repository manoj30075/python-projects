
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def add_neighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def get_connections(self):
        self.connectedTo.keys()


