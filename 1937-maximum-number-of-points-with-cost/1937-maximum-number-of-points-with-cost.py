class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        current_points = [point for point in points[0]]
        
        for row in range(1, len(points)):
            max_col_points = -float("inf")
            for col in range(0, len(current_points)):
                max_col_points = max(max_col_points - 1, current_points[col])
                current_points[col] = max_col_points

            max_col_points = -float("inf")
            for col in range(len(current_points) - 1, -1, -1):
                max_col_points = max(max_col_points - 1, current_points[col])
                current_points[col] = max_col_points

            for col in range(len(current_points)):
                current_points[col] = points[row][col] + current_points[col]
                
        return max(current_points)