def get_diff(l1, l2):
    list = set()
    for element in l1:
        if element not in l2:
            list.add(element)
    return list

def dfs_walk(graph, start):
    visited, stack = set(), [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(get_diff(graph[node], visited))
    return visited

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in get_diff(graph[vertex], set(path)):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print(dfs_walk(graph, 'D'))
gen = dfs_paths(graph, 'F', 'D')
for i in gen:
    print(i)