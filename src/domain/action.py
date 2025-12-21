from src.domain.state import State


class Action:
    def __init__(self, name, preconditions, add_effects, del_effects):
        self.name = name
        self.pre = set(preconditions)
        self.add = set(add_effects)
        self.delete = set(del_effects)

    def is_applicable(self, state: State):
        return self.pre.issubset(state.predicates)

    def apply(self, state: State):
        new_state = set(state.predicates)
        new_state -= self.delete
        new_state |= self.add
        return State(new_state)
