class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = [[] for _ in range(n)]
        for i in range(len(edges)):
            u, v = edges[i]
            c = succProb[i]
            adj[u].append((v, c))
            adj[v].append((u, c))

        dist = [0.0] * n
        visited = [False] * n
        maxHeap = [(-1.0, start_node)]
        dist[start_node] = 1.0

        while maxHeap:
            w, u = heapq.heappop(maxHeap)
            if visited[u]:
                continue
            visited[u] = True

            for v, c in adj[u]:
                if not visited[v] and c * (-w) > dist[v]:
                    dist[v] = c * (-w)
                    heapq.heappush(maxHeap, (-dist[v], v))

        return dist[end_node]
        