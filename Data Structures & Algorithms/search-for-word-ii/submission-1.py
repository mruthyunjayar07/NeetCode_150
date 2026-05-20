class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node['end'] = word

        ROWS, COLS = len(board), len(board[0])
        res = []

        def backtrack(r, c, node):
            ch = board[r][c]
            if ch not in node:
                return

            next_node = node[ch]

            if 'end' in next_node:
                res.append(next_node['end'])
                del next_node['end']

            board[r][c] = '#'

            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != '#':
                    backtrack(nr, nc, next_node)

            board[r][c] = ch

            if not next_node:
                del node[ch]

        for r in range(ROWS):         
            for c in range(COLS):
                backtrack(r, c, trie)

        return res                    