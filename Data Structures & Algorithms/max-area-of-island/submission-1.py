class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        res = 0

        def bfs(r, c):
            temp = 1

            q = deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                r, c = q.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in directions:
                    row, col = r+dr, c+dc

                    if (row in range(rows)
                        and col in range(cols)
                        and grid[row][col] == 1
                        and (row, col) not in visit):
                            q.append((row, col))
                            visit.add((row, col))
                            temp = temp + 1

            return temp

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r, c) not in visit:
                    temp = bfs(r, c)
                    res = max(temp, res)

        return res
    