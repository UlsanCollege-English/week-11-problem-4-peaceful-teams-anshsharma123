from collections import deque

def bipartition(graph):
    """
    Return (left_set, right_set) if bipartite; else None.
    BFS coloring over all components.
    """
    color = {}   # node -> 0 or 1

    for start in graph:
        if start not in color:
            # Begin BFS for a new component
            color[start] = 0
            queue = deque([start])

            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if v not in color:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    else:
                        # Conflict: same color on an edge
                        if color[v] == color[u]:
                            return None

    # If we reach here, coloring succeeded
    left  = {u for u in color if color[u] == 0}
    right = {u for u in color if color[u] == 1}
    return left, right
