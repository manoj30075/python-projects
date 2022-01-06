"""
file: icemaze.py
description: An implementation of a Get of the ICE maze

language: python3

author: Koteswara Rao Bade (kb5608)
author: Snehil Sharma (ss7696)

"""

import sys

from Lab9.vertex import Vertex
from graph import Graph


class IceMaze:
    ROCK = '*'

    def findNeighbors(self, row, column, grid):
        """
        Finds the neighbors of a given vertex
        :param row: row number of the vertex
        :param column: column number of the vertex
        :param grid: the given grid
        :return: neighbors of the vertex as a tuple
        """
        # initialize neighbors to None
        left_neighbor, right_neighbor, up_neighbor, down_neighbor = None, None, None, None

        # check left neighbor
        i = column + 1
        while len(grid[0]) > i:
            # if the vertex is a rock,set previous vertex as right neighbor
            if grid[row][i] == IceMaze.ROCK:
                # condition for not setting same vertex as neighbor
                if i - 1 != column:
                    right_neighbor = (row, i - 1)
                break
            # if edge is found set that as right neighbor
            if i == len(grid[0]) - 1:
                right_neighbor = (row, i)
                break
            i += 1

        # check right neighbor
        i = column - 1
        while i >= 0:
            # if the vertex is a rock,set previous vertex as left neighbor
            if grid[row][i] == IceMaze.ROCK:
                # condition for not setting same vertex as neighbor
                if (i + 1) != column:
                    left_neighbor = (row, i + 1)
                break
            # if edge is found set that as left neighbor
            if i == 0:
                left_neighbor = (row, i)
                break
            i -= 1

        # check down neighbor
        i = row + 1
        while i < len(grid):
            # if the vertex is a rock,set previous vertex as down neighbor
            if grid[i][column] == IceMaze.ROCK:
                # condition for not setting same vertex as neighbor
                if i - 1 != row:
                    down_neighbor = (i - 1, column)
                break
            # if edge is found set that as down neighbor
            if i == len(grid) - 1:
                down_neighbor = (i, column)
                break
            i += 1

        # check up neighbor
        i = row - 1
        while i >= 0:
            # if the vertex is a rock,set previous vertex as up neighbor
            if grid[i][column] == IceMaze.ROCK:
                # condition for not setting same vertex as neighbor
                if i + 1 != row:
                    up_neighbor = (i + 1, column)
                break
            # if edge is found set that as up neighbor
            if i == 0:
                up_neighbor = (i, column)
                break
            i -= 1

        return left_neighbor, right_neighbor, up_neighbor, down_neighbor

    def construct_path_map(self, escape_vertex, graph):
        """
        Constructs a map of the shortest path from the start vertex to the escape vertex.
        :param escape_vertex: the escape vertex
        :param graph: the graph
        :return:
        """
        # initialize the path map with number of edges
        # as keys and the value as list of vertices
        path_map = {}

        # looping through the vertices
        for vertex in graph.getVertices():
            if vertex == escape_vertex:
                continue
            # find the shortest path from the start vertex to the escape vertex
            shortest_path = self.findShortestPath(graph.getVertex(vertex), graph.getVertex(escape_vertex))
            # reverse the vertex
            new_vertex = (vertex[1], vertex[0])
            # initialize the number of edges to zero
            number_of_edges = 0
            # if path is found set the number of edges
            if shortest_path is not None:
                number_of_edges = len(shortest_path) - 1

            # add the vertex to the path map
            if path_map.get(number_of_edges) is None:
                path_map[number_of_edges] = [new_vertex]
            else:
                path_map[number_of_edges].append(new_vertex)

        return path_map

    def findShortestPath(self, start, end):
        """
        Find the shortest path, if one exists, between a start and end vertex
        :param start: (Vertex): the start vertex
        :param end: (Vertex): the destination vertex
        :return: A list of Vertex objects from start to end, if a path exists,
            otherwise None
        """
        # Using a queue as the dispenser type will result in a breadth first
        # search
        queue = [start]

        # The predecessor dictionary maps the current Vertex object to its
        # immediate predecessor.  This collection serves as both a visited
        # construct, as well as a way to find the path
        predecessors = {start: None}

        # Loop until either the queue is empty, or the end vertex is encountered
        while len(queue) > 0:
            current = queue.pop(0)
            if current == end:
                break
            for neighbor in current.getConnections():
                if neighbor not in predecessors:  # if neighbor unvisited
                    predecessors[neighbor] = current  # map neighbor to current
                    queue.append(neighbor)  # enqueue the neighbor

        # If the end vertex is in predecessors a path was found
        if end in predecessors:
            path = []
            current = end
            while current != start:  # loop backwards from end to start
                path.insert(0, current)  # prepend current to the path list
                current = predecessors[current]  # move to the predecessor
            path.insert(0, start)
            return path
        else:
            return None

    def build_graph(self, grid, exit_vertex):
        """
        Builds a graph from a file.
        """
        ice_pond_graph = Graph()
        # loop through the grid
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                # if vertex is not the rock, find neighbors and add it to the graph
                if grid[row][column] == '.':
                    # if vertex is not already in the graph, add it
                    if ice_pond_graph.getVertex((row, column)) is None:
                        ice_pond_graph.addVertex((row, column))
                    # get the neighbors of the vertex
                    left_neighbor, right_neighbor, up_neighbor, down_neighbor = \
                        self.findNeighbors(row, column, grid)
                    # add all the neighbors to the graph
                    if left_neighbor:
                        ice_pond_graph.addEdge((row, column), left_neighbor)

                    if right_neighbor is None:
                        # adding escape vertex as a right neighbor to the exit vertex
                        if (row, column) == exit_vertex:
                            right_neighbor = (exit_vertex[0], exit_vertex[1] + 1)
                            ice_pond_graph.addEdge((row, column), right_neighbor)
                    elif right_neighbor == exit_vertex:
                        right_neighbor = (exit_vertex[0], exit_vertex[1] + 1)
                        ice_pond_graph.addEdge((row, column), right_neighbor)
                    else:
                        ice_pond_graph.addEdge((row, column), right_neighbor)

                    if up_neighbor:
                        ice_pond_graph.addEdge((row, column), up_neighbor)
                    if down_neighbor:
                        ice_pond_graph.addEdge((row, column), down_neighbor)
                else:
                    # if vertex is rock, add it to the graph
                    if ice_pond_graph.getVertex((row, column)) is None:
                        ice_pond_graph.addVertex((row, column))
        return ice_pond_graph

    def get_pond(self, file_name):
        """
        Reads a file and returns a grid of the pond.
        :param file_name:
        :return:
        """
        with open(file_name) as f:
            # return first line to get the grid size and the escape vertex
            first_line = f.readline().strip()
            grid = []
            for line in f:
                # add each line as a list to the grid
                line = line.strip().split()
                grid.append(line)
        return grid, first_line

    def print_result(self, path_map):
        """
        Prints the result of the pond.
        :param path_map:
        :return: None
        """
        for key in sorted(path_map.keys()):
            # key is zero means there is no path for those vertices
            if key != 0:
                print(key, ':', path_map[key])
        # printing no path vertices
        if 0 in path_map:
            print("No path", ':', path_map[0])

    def start_finding_escape_paths(self):
        # Get the pond grid and the escape vertex
        pond_structure, first_line = self.get_pond(sys.argv[1])
        escape_row = int(first_line.split()[2])
        exit_vertex = (escape_row, len(pond_structure[0]) - 1)
        escape_vertex = (escape_row, len(pond_structure[0]))

        # Build the graph
        graph = self.build_graph(pond_structure, exit_vertex)

        # constructing the path map
        final_map = self.construct_path_map(escape_vertex, graph)

        # printing the result map
        self.print_result(final_map)


def main():
    """
    Main function.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 pond.py <file_name>")
        sys.exit(1)

    # Start finding escape paths
    IceMaze().start_finding_escape_paths()


if __name__ == '__main__':
    main()
