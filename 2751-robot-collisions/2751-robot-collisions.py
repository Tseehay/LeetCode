class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        indices = sorted(range(n), key=lambda x: positions[x])
        result = []
        stack = deque()

        for current_index in indices:
            if directions[current_index] == "R":
                stack.append(current_index)
            else:
                while stack and healths[current_index] > 0:
                    top_index = stack.pop()
                    if healths[top_index] > healths[current_index]:
                        healths[top_index] -= 1
                        healths[current_index] = 0
                        stack.append(top_index)
                    elif healths[top_index] < healths[current_index]:
                        healths[current_index] -= 1
                        healths[top_index] = 0
                    else:
                        healths[current_index] = 0
                        healths[top_index] = 0

        for index in range(n):
            if healths[index] > 0:
                result.append(healths[index])

        return result