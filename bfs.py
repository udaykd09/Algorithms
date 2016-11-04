def get_diff(l1, l2):
    list = set()
    for element in l1:
        if element not in l2:
            list.add(element)
    return list

def bfs_walk(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex]-visited)
    return visited


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in get_diff(graph[vertex], path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print(bfs_walk(graph, 'A'))
gen = bfs_paths(graph, 'A', 'D')
for i in gen:
    print(i)