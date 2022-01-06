
def bfs(start, end):
    queue = []
    queue.append(start)

    predesessor_map = {}
    predesessor_map[start] = None

    while len(queue) > 0:
        current = queue.pop(0)

        if current == end:
            break

        for neighbor in current.getConnections():
            if neighbor not in predesessor_map:
                predesessor_map[neighbor] = current
                queue.append(neighbor)

    if end in predesessor_map:
        path = []
        current = end

        while current != start:
            path.insert(0, current)
            current = predesessor_map[current]

        path.insert(0, start)
        return path
    else:
        return None


def _dfs(current, end, visited):
    if current == end:
        return [current]
    for neighbor in current.getConnections:
        if neighbor not in visited:
            visited.add(neighbor)
            path = _dfs(neighbor, end, visited)

            if path != None:
                return path.insert(0, neighbor)

    return None


def dfs(start, end):
    visited = set()
    visited.add(start)

    return _dfs(start, end, visited)