class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0

        def neighbors(state):
            for i in range(4):
                digit = int(state[i])
                for move in (-1, 1):
                    new_digit = (digit + move) % 10
                    yield state[:i] + str(new_digit) + state[i+1:]

        queue = deque([("0000", 0)])  # (state, steps)
        visited = set(["0000"])

        while queue:
            state, steps = queue.popleft()
            if state == target:
                return steps
            for nxt in neighbors(state):
                if nxt not in visited and nxt not in dead:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))

        return -1