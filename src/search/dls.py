from src.domain.node import Node

def dls(node, goal, actions, limit, visited, perf):
    perf.expanded += 1

    if goal.issubset(node.state.predicates):
        return node

    if limit == 0:
        return None

    state_key = frozenset(node.state.predicates)
    visited.add(state_key)

    for action in actions:
        if action.is_applicable(node.state):
            new_state = action.apply(node.state)
            new_key = frozenset(new_state.predicates)

            if new_key not in visited:
                perf.explored += 1
                child = Node(new_state, node, action)
                result = dls(child, goal, actions, limit - 1, visited, perf)
                if result:
                    return result

    return None
