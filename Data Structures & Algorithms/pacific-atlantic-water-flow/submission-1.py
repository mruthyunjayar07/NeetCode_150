from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        ROWS, COLS = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, visited):
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    nr < 0 or nr >= ROWS or
                    nc < 0 or nc >= COLS or
                    (nr, nc) in visited or
                    heights[nr][nc] < heights[r][c]
                ):
                    continue

                dfs(nr, nc, visited)

        # Pacific borders
        for c in range(COLS):
            dfs(0, c, pacific)
            dfs(ROWS - 1, c, atlantic)

        for r in range(ROWS):
            dfs(r, 0, pacific)
            dfs(r, COLS - 1, atlantic)

        ans = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    ans.append([r, c])

        return ans