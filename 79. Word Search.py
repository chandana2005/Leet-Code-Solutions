class Solution(object):
    def exist(self, board, word):
        from collections import Counter
        
        row = len(board)
        col = len(board[0])
        
        board_letters = Counter(c for r in board for c in r)
        word_letters = Counter(word)
        for c in word_letters:
            if word_letters[c] > board_letters.get(c, 0):
                return False
        
        def dfs(i, j, index):
            if index == len(word):
                return True
            if i < 0 or j < 0 or i >= row or j >= col or board[i][j] != word[index]:
                return False
            temp = board[i][j]
            board[i][j] = '#' 
          
            found = (
                dfs(i+1, j, index+1) or
                dfs(i-1, j, index+1) or
                dfs(i, j+1, index+1) or
                dfs(i, j-1, index+1)
            )
            board[i][j] = temp 
            return found
        
     
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
