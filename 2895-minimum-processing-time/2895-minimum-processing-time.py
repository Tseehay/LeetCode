class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks, processorTime, ans = sorted(tasks), sorted(processorTime), 0
        for i in processorTime:
            ans = max(ans, i + max(tasks[-4:]))
            tasks = tasks[:-4]
        return ans