class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def extract_plan(self):
        actions = []
        node = self
        while node.parent:
            actions.append(node.action.name)
            node = node.parent
        return list(reversed(actions))
