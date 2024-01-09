class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0: # if out of bounds or position in grid is water
                return 1

            if (i, j) in visited:
                return 0 # if already visited, move on
            
            visited.add((i, j))
            perimeter = dfs(i, j + 1)
            perimeter += dfs(i + 1, j)
            perimeter += dfs(i, j - 1)
            perimeter += dfs(i - 1, j)

            return perimeter

        # now we need to initialize the recursion by iterating and finding
        # a piece of land to begin with
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    return dfs(i, j)

