class State:
    def __init__(self, predicates):
        self.predicates = frozenset(predicates)

    def __contains__(self, item):
        return item in self.predicates

    def __eq__(self, other):
        return self.predicates == other.predicates

    def __hash__(self):
        return hash(self.predicates)
