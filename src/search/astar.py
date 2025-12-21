import heapq
from src.domain.node import Node
from src.heuristics.blocks_heuristic import blocks_heuristic

def astar(initial_state, goal, actions, perf):
    counter = 0
    frontier = []
    root = Node(initial_state)
    heapq.heappush(frontier, (0, counter, root))
    counter += 1

    explored = {}

    while frontier:
        _, _, node = heapq.heappop(frontier)
        perf.expanded += 1

        if goal.issubset(node.state.predicates):
            return node.extract_plan()

        state_key = frozenset(node.state.predicates)
        explored[state_key] = node.cost

        for action in actions:
            if action.is_applicable(node.state):
                new_state = action.apply(node.state)
                new_key = frozenset(new_state.predicates)
                new_cost = node.cost + 1

                if new_key not in explored or explored[new_key] > new_cost:
                    perf.explored += 1
                    h = blocks_heuristic(new_state, goal)
                    f = new_cost + h
                    child = Node(new_state, node, action, new_cost)
                    heapq.heappush(frontier, (f, counter, child))
                    counter += 1

    return None
