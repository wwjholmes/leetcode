#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#
# https://leetcode.com/problems/text-justification/description/
#
# algorithms
# Hard (29.68%)
# Likes:    939
# Dislikes: 1888
# Total Accepted:    162.1K
# Total Submissions: 544.5K
# Testcase Example:  '["This", "is", "an", "example", "of", "text", "justification."]\n16'
#
# Given an array of words and a width maxWidth, format the text such that each
# line has exactly maxWidth characters and is fully (left and right)
# justified.
#
# You should pack your words in a greedy approach; that is, pack as many words
# as you can in each line. Pad extra spaces SPACE when necessary so that each
# line has exactly maxWidth characters.
#
# Extra spaces between words should be distributed as evenly as possible. If
# the number of spaces on a line do not divide evenly between words, the empty
# slots on the left will be assigned more spaces than the slots on the right.
#
# For the last line of text, it should be left justified and no extra space is
# inserted between words.
#
# Note:
#
#
# A word is defined as a character sequence consisting of non-space characters
# only.
# Each word's length is guaranteed to be greater than 0 and not exceed
# maxWidth.
# The input array words contains at least one word.
#
#
#
# Example 1:
#
#
# Input: words = ["This", "is", "an", "example", "of", "text",
# "justification."], maxWidth = 16
# Output:
# [
# "This    is    an",
# "example  of text",
# "justification.  "
# ]
#
# Example 2:
#
#
# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth =
# 16
# Output:
# [
# "What   must   be",
# "acknowledgment  ",
# "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall
# be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified becase it contains only one
# word.
#
# Example 3:
#
#
# Input: words =
# ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],
# maxWidth = 20
# Output:
# [
# "Science  is  what we",
# ⁠ "understand      well",
# "enough to explain to",
# "a  computer.  Art is",
# "everything  else  we",
# "do                  "
# ]
#
#
# Constraints:
#
#
# 1 <= words.length <= 300
# 1 <= words[i].length <= 20
# words[i] consists of only English letters and symbols.
# 1 <= maxWidth <= 100
# words[i].length <= maxWidth
#
#
#

# @lc code=start
from typing import List

SPACE = ''
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        text = []
        stats = []
        line = []
        count = 0

        # split into lines
        while words:
            word = words.pop(0)
            line.append(word)
            count = self.count(line)
            if count > maxWidth:
                line.pop(-1)
                text.append(line)
                stats.append(self.count(line))
                line = [word]
            elif count == maxWidth:
                text.append(line)
                stats.append(count)
                line = []
        if line:
            text.append(line)
            stats.append(count)

        # format each line
        formatted_text = []
        last_line = text.pop(-1)
        for index, line in enumerate(text):
            count = stats[index]
            gap = maxWidth - count
            if len(line) == 1:
                word = line[0]
                formatted_text.append(word + SPACE * (maxWidth - len(word)))
            else:
                even_space = gap // (len(line) - 1)
                module = gap % (len(line) - 1)
                formatted_line = ""
                for i, word in enumerate(line):
                    if i == 0:
                        formatted_line += word
                    elif i <= module:
                        formatted_line += " " * (even_space + 2) + word
                    else:
                        formatted_line += " " * (even_space + 1) + word
                formatted_text.append(formatted_line)

        # format last line separtely
        last_line = SPACE.join(last_line)
        if len(last_line) < maxWidth:
            last_line += SPACE * (maxWidth - len(last_line))
        
        # append last line
        formatted_text.append(last_line)

        return  formatted_text

    def count(self, words: List[str]) -> int:
        count = 0
        for w in words:
            count += len(w) + 1
        return count - 1


s = Solution()
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(s.fullJustify(words, maxWidth))

# @lc code=end
