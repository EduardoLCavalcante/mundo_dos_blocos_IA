class PredicateMap:
    def __init__(self):
        self._map = {}
        self._counter = 1

    def get(self, predicate: str) -> int:
        if predicate not in self._map:
            self._map[predicate] = self._counter
            self._counter += 1
        return self._map[predicate]

    def decode(self, value: int) -> str:
        for k, v in self._map.items():
            if v == value:
                return k
        return "UNKNOWN"
