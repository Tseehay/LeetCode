class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        dead_set = set(deadends)
        if "0000" in dead_set:
            return -1

        queue = deque([('0000', 0)])
        visited = set(['0000'])

        while queue:
            current, moves = queue.popleft()

            if current == target:
                return moves

            for i in range(4):
                for delta in (-1, 1):  # Try both increment and decrement
                    new_wheel_value = (int(current[i]) + delta) % 10
                    new_state = current[:i] + str(new_wheel_value) + current[i+1:]

                    if new_state not in visited and new_state not in dead_set:
                        visited.add(new_state)
                        queue.append((new_state, moves + 1))

        return -1
