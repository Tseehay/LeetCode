class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        n_sum = sum(rolls)
        m_sum = mean * (n + len(rolls)) - n_sum

        if m_sum > 6 * n or m_sum < n:
            return []

        res = [m_sum // n] * n

        for i in range(m_sum % n):
            res[i] += 1

        return res