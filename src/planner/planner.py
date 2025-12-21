from src.search.bfs import bfs
from src.search.ids import ids
from src.search.astar import astar
from src.search.bidirectional import bidirectional

class Planner:
    def __init__(self, initial_state, goal, actions):
        self.initial_state = initial_state
        self.goal = goal
        self.actions = actions

    def solve(self, algorithm, perf):
        if algorithm == "BFS":
            return bfs(self.initial_state, self.goal, self.actions, perf)

        if algorithm == "IDS":
            return ids(self.initial_state, self.goal, self.actions, perf)

        if algorithm == "ASTAR":
            return astar(self.initial_state, self.goal, self.actions, perf)

        if algorithm == "BIDIR":
            return bidirectional(self.initial_state, self.goal, self.actions, perf)

        raise ValueError("Algoritmo não suportado")
