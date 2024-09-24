class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for value in range(len(arr), 0, -1):
            idx = arr.index(value)
            if idx != value - 1:
                if idx != 0:
                    arr[:idx + 1] = reversed(arr[:idx + 1])
                    res.append(idx + 1)
                arr[:value] = reversed(arr[:value])
                res.append(value)
        return res