from collections import deque
from src.domain.node import Node

def bidirectional(initial_state, goal, actions, perf):
    """
    Busca Bidirecional (implementação limitada para STRIPS)
    """

    front = deque([Node(initial_state)])
    visited = set()

    while front:
        node = front.popleft()
        perf.expanded += 1

        if goal.issubset(node.state.predicates):
            return node.extract_plan()

        state_key = frozenset(node.state.predicates)
        visited.add(state_key)

        for action in actions:
            if action.is_applicable(node.state):
                new_state = action.apply(node.state)
                new_key = frozenset(new_state.predicates)

                if new_key not in visited:
                    perf.explored += 1
                    front.append(Node(new_state, node, action))

    return None
