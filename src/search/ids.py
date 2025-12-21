from src.domain.node import Node
from src.search.dls import dls

def ids(initial_state, goal, actions, perf, max_depth=50):
    for depth in range(max_depth):
        root = Node(initial_state)
        visited = set()
        result = dls(root, goal, actions, depth, visited, perf)
        if result:
            return result.extract_plan()
    return None
