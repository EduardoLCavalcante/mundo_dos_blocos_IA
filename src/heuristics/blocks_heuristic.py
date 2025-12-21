def blocks_heuristic(state, goal):
    misplaced = 0
    for g in goal:
        if g not in state.predicates:
            misplaced += 1
    return misplaced
