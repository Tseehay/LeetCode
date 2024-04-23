class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]  # Only one node, which is its own MHT root
    
        # Build adjacency list for the tree
        adj = defaultdict(list)
        degrees = [0] * n

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            degrees[a] += 1
            degrees[b] += 1

        # Start with all nodes with degree 1 (leaves)
        leaves = deque([i for i in range(n) if degrees[i] == 1])
        remaining_nodes = n

        while remaining_nodes > 2:
            num_leaves = len(leaves)
            remaining_nodes -= num_leaves

            for _ in range(num_leaves):
                leaf = leaves.popleft()
                for neighbor in adj[leaf]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        leaves.append(neighbor)

        # The remaining nodes in the leaves deque are the roots of the MHTs
        return list(leaves)