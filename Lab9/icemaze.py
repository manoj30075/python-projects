from graph import Graph
import sys


def findNeighbors(row, column, matrix):
    """
    Finds the neighbors of a given vertex.
    :param row:
    :param column:
    :param matrix:
    :return:
    """
    left_neighbor = None
    right_neighbor = None
    up_neighbor = None
    down_neighbor = None

    temp = column + 1
    while len(matrix[0]) > temp:
        if matrix[row][temp] == '*':
            if (temp - 1) != column:
                right_neighbor = (row, temp - 1)
            break
        if temp == len(matrix[0]) - 1:
            right_neighbor = (row, temp)
            break
        temp += 1

    temp = column - 1

    while temp >= 0:
        if matrix[row][temp] == '*':
            if (temp + 1) != column:
                left_neighbor = (row, temp + 1)
            break
        if temp == 0:
            left_neighbor = (row, temp)
            break
        temp -= 1

    temp = row + 1

    while temp < len(matrix):
        if matrix[temp][column] == '*':
            if temp - 1 != row:
                down_neighbor = (temp - 1, column)
            break
        if temp == len(matrix) - 1:
            down_neighbor = (temp, column)
            break
        temp += 1

    temp = row - 1

    while temp >= 0:
        if matrix[temp][column] == '*':
            if temp + 1 != row:
                up_neighbor = (temp + 1, column)
            break
        if temp == 0:
            up_neighbor = (temp, column)
            break
        temp -= 1

    return left_neighbor, right_neighbor, up_neighbor, down_neighbor


def construct_path(out_vertex, ice_maze_graph):
    """
    Constructs a path map for the given graph.
    :param escape_vertex:
    :param ice_maze_graph:
    :return:
    """
    path_map = {}
    for vertex in ice_maze_graph.getVertices():
        if vertex == out_vertex:
            continue
        path = findShortestPath(ice_maze_graph.getVertex(vertex), ice_maze_graph.getVertex(out_vertex))
        new_vertex = (vertex[1], vertex[0])
        edges = 0
        if path is not None:
            edges = len(path) - 1

        if path_map.get(edges) is None:
            path_map[edges] = [new_vertex]
        else:
            path_map[edges].append(new_vertex)

    for key in sorted(path_map.keys()):
        if key != 0:
            print(key, ':', path_map[key])
    if 0 in path_map:
        print("No path", ':', path_map[0])


def findShortestPath(start, end):
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



def build_graph(matrix, out_vertex):
    """
    Build a graph using grid
    :param grid:
    :return:
    """
    maze_graph = Graph()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '.':
                if maze_graph.getVertex((i, j)) is None:
                    maze_graph.addVertex((i, j))
                left_neighbor, right_neighbor, up_neighbor, down_neighbor = \
                    findNeighbors(i, j, matrix)
                if left_neighbor:
                    maze_graph.addEdge((i, j), left_neighbor)
                if right_neighbor is None:
                    if (i, j) == out_vertex:
                        right_neighbor = (out_vertex[0], out_vertex[1] + 1)
                        maze_graph.addEdge((i, j), right_neighbor)
                    elif right_neighbor == out_vertex:
                        right_neighbor = (out_vertex[0], out_vertex[1] + 1)
                        maze_graph.addEdge((i, j), right_neighbor)
                    else:
                        maze_graph.addEdge((i, j), right_neighbor)
                if up_neighbor:
                    maze_graph.addEdge((i, j), up_neighbor)
                if down_neighbor:
                    maze_graph.addEdge((i, j), down_neighbor)
            else:
                if maze_graph.getVertex((i, j)) is None:
                    maze_graph.addVertex((i, j))
    return maze_graph


def process_file(file_name):
    with open(file_name) as f:
        grid = []
        for line in f:
            line = line.strip()
            line = line.split()
            grid.append(line)

        return grid


def main():
    """
    Main function.
    """

    if len(sys.argv) != 2:
        print("Usage: python ice_rock_game.py maze_file")
        sys.exit(1)

    file_name = sys.argv[1]
    grid = process_file(file_name)
    grid_properties = grid[0]
    out_row = int(grid_properties[2])
    out_vertex = (out_row, len(grid[1]) - 1)
    ice_maze_graph = build_graph(grid[1:], out_vertex)
    construct_path(out_vertex, ice_maze_graph)


if __name__ == '__main__':
    main()
