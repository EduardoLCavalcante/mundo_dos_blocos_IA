from collections import deque
from src.domain.node import Node

def bfs(initial_state, goal, actions, performance):
    frontier = deque()
    explored = set()

    root = Node(initial_state)
    frontier.append(root)
    explored.add(initial_state)

    performance.explored = 1

    while frontier:
        node = frontier.popleft()
        performance.expanded += 1

        if goal.issubset(node.state.predicates):
            return node.extract_plan()

        for action in actions:
            if action.is_applicable(node.state):
                new_state = action.apply(node.state)
                if new_state not in explored:
                    explored.add(new_state)
                    performance.explored += 1
                    frontier.append(Node(new_state, node, action))

    return None
