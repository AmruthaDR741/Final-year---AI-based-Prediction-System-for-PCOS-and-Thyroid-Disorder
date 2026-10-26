"""Breadth-First Search (BFS) is a graph traversal algorithm that explores a data structure systematically, 
layer by layer, starting from a chosen node. By using a queue to track nodes, it evaluates all direct neighbors
first before moving to deeper connections, making it ideal for finding the absolute shortest path"""


from collections import deque

def bfs(graph , start ):
    visited = {start}
    queue = deque([start])
    order = []

    while queue :
        node = queue.popleft()
        order.append(node)

        for nbr in graph[node]:
            if nbr not in visited :
                visited.add(nbr)
                queue.append(nbr)
    return order
