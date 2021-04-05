#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (37.03%)
# Likes:    3581
# Dislikes: 142
# Total Accepted:    291.3K
# Total Submissions: 778.7K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
#  '["oath","pea","eat","rain"]'
#
# Given an m x n board of characters and a list of strings words, return all
# words on the board.
# 
# Each word must be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once in a word.
# 
# 
# Example 1:
# 
# 
# Input: board =
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# 
# 
# Example 2:
# 
# 
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.
# 
# 
#
from collections import defaultdict
from typing import List

# @lc code=start


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        start_points = defaultdict(list)
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                cells = start_points[board[i][j]]
                cells.append((i, j))
        visited = [[False for j in range(n)]for i in range(m)]
        words_set = set()
        for word in words:
            for [x, y] in start_points[word[0]]:
                if self.findWord(board, visited, word, 0, x, y):
                    words_set.add(word)
        return list(words_set)

    def findWord(self, board: List[List[str]], visited: List[List[bool]], word: str, idx: int, x: int, y: int) -> bool:
        if word[idx] != board[x][y]:
            return False
        elif idx == len(word) - 1:
            return True 

        visited[x][y] = True
        idx += 1

        found = False
        for [dx, dy] in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x = x + dx
            new_y = y + dy
            if new_x < 0 or new_x >= len(board) or new_y < 0 or new_y >= len(board[0]):
                continue
            elif visited[new_x][new_y]:
                continue
            elif self.findWord(board, visited, word, idx, new_x, new_y):
                found = True

        visited[x][y] = False
        return found


# @lc code=end

s = Solution()
board = [["a","b"],["c","d"]]
words = ["abcb"]
board = [["a"]]
words = ["a"]
board = [["a","b"],["c","d"]]
words = ["abcb"]
board = [["o", "a", "a", "n"], ["e", "t", "a", "e"],
         ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]
board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
words = ["oa","oaa"]
print(s.findWords(board, words))
