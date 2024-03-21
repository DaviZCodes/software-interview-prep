class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        if not grid:
            return max_area
        
        visited_nodes = set() # (i, j)

        rows = len(grid)
        columns = len(grid[0])

        #bfs 
        def bfs(i, j):
            q = collections.deque()

            visited_nodes.add((i,j))
            q.append((i,j))

            currMaxArea = 1 # starting at 1 since we pass in first node

            while q:
                row, column = q.popleft()
                directions = [[-1,0], [1,0], [0,-1], [0,1]]

                for dr, dc in directions:
                    r = row + dr
                    c = column + dc

                    if r in range(rows) and c in range(columns) and grid[r][c] == 1 and (r,c) not in visited_nodes:
                        visited_nodes.add((r,c))
                        q.append((r,c))
                        currMaxArea += 1
            
            return currMaxArea

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1 and (i, j) not in visited_nodes:
                    max_area = max(max_area, bfs(i, j))
        
        return max_area

        
