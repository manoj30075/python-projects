import graph
import sys


def process_file(file_name: str):
    """
    Pushes all the strings into an array
    :param file_name: file name which has to be processed
    :return: returns array of strings
    """
    file_values = []
    with open(file_name) as f:
        for line in f:
            file_values.append(line.strip())

    return file_values


def find_neighbors(matrix, i, j):
    """
    Finds the neighbors of the given vertex
    :param matrix: matrix which has to be processed
    :param i: row index
    :param j: column index
    :return: returns the neighbors of the given vertex
    """
    left_neighbor = None
    right_neighbor = None
    top_neighbor = None
    bottom_neighbor = None

    left_list = [x for x in range(j, -1, -1)]
    right_list = [x for x in range(j, len(matrix[i]))]
    top_list = [x for x in range(i, -1, -1)]
    bottom_list = [x for x in range(i, len(matrix))]

    for x in left_list:
        if matrix[i][x] == '*':
            left_neighbor = (i, x)
            break

    for x in right_list:
        if matrix[i][x] == '*':
            right_neighbor = (i, x)
            break

    for x in top_list:
        if matrix[x][j] == '*':
            top_neighbor = (x, j)
            break

    for x in bottom_list:
        if matrix[x][j] == '*':
            bottom_neighbor = (x, j)
            break

    return left_neighbor, right_neighbor, top_neighbor, bottom_neighbor


def build_graph(matrix):
    """
    Builds the graph from the matrix
    :param matrix: matrix which has to be converted to graph
    :return: returns the graph
    """
    ice_rock_graph = graph.Graph()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != '*':
                if (i, j) not in ice_rock_graph.vertList:
                    ice_rock_graph.add_vertex((i, j))
                left_neighbor, right_neighbor, top_neighbor, bottom_neighbor = find_neighbors(matrix, i, j)
                if left_neighbor:
                    ice_rock_graph.add_edge((i, j), left_neighbor)
                if right_neighbor:
                    ice_rock_graph.add_edge((i, j), right_neighbor)
                if top_neighbor:
                    ice_rock_graph.add_edge((i, j), top_neighbor)
                if bottom_neighbor:
                    ice_rock_graph.add_edge((i, j), bottom_neighbor)
    return graph


def main():
    """
    Main function
    :return: None
    """

    if len(sys.argv) != 2:
        print("Usage: ice_rock.py <filename>")
        sys.exit(1)

    file_name = sys.argv[1]
    file_values = process_file(file_name)
    ice_rock_matrix = file_values[1:]
    ice_rock_matrix = [x.split(" ") for x in ice_rock_matrix]

    ice_rock_matrix_graph = build_graph(ice_rock_matrix)


if __name__ == "__main__":
    main()