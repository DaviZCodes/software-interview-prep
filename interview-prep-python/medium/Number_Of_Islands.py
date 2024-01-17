'''
Return number of islands "1" in graph
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: # if none, return 0
            return 0 
        
        rows, columns = len(grid), len(grid[0])
        visited = set() # unique set that takes in a tuple (x, y)
        number_islands = 0

        def bfs(i, j): # create a bfs function that accepts a coordinate
            q = collections.deque() # use collections.deque() which has .popleft()
            '''
            take element from queue, add new element to to visited, 
            and add it to queue
            '''
            visited.add((i, j))
            q.append((i,j))

            while q: 
                # we want to traverse the whole queue which signifies one island
                row, column = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] 
                #right, left, up, down

                for dr, dc in directions:
                    r, c = row + dr, column + dc
                    if ((r) in range(rows) and (c) in range(columns)
                    and grid[r][c] == "1" and (r, c) not in visited):
                        '''
                        With bfs, if element is "1" and not in visited, we want
                        to add to queue and add to visited
                        '''
                        q.append((r, c))
                        visited.add((r, c))

        for row in range(rows): # iterate through entire 2d graph and perform bfs
            for column in range(columns):
                if grid[row][column] == "1" and (row, column) not in visited:
                    bfs(row, column)
                    number_islands += 1 # only after each bfs, we increment
        
        return number_islands
                    
