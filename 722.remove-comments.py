#
# @lc app=leetcode id=722 lang=python3
#
# [722] Remove Comments
#
# https://leetcode.com/problems/remove-comments/description/
#
# algorithms
# Medium (36.07%)
# Likes:    450
# Dislikes: 1163
# Total Accepted:    41.2K
# Total Submissions: 113.6K
# Testcase Example:  '["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]'
#
# Given a C++ program, remove comments from it. The program source is an array
# where source[i] is the i-th line of the source code.  This represents the
# result of splitting the original source code string by the newline character
# \n.
#
# In C++, there are two types of comments, line comments, and block comments.
#
# The string // denotes a line comment, which represents that it and rest of
# the characters to the right of it in the same line should be ignored.
#
# The string /* denotes a block comment, which represents that all characters
# until the next (non-overlapping) occurrence of */ should be ignored.  (Here,
# occurrences happen in reading order: line by line from left to right.)  To be
# clear, the string /*/ does not yet end the block comment, as the ending would
# be overlapping the beginning.
#
# The first effective comment takes precedence over others: if the string //
# occurs in a block comment, it is ignored. Similarly, if the string /* occurs
# in a line or block comment, it is also ignored.
#
# If a certain line of code is empty after removing comments, you must not
# output that line: each string in the answer list will be non-empty.
#
# There will be no control characters, single quote, or double quote
# characters.  For example, source = "string s = "/* Not a comment. */";" will
# not be a test case.  (Also, nothing else such as defines or macros will
# interfere with the comments.)
#
# It is guaranteed that every open block comment will eventually be closed, so
# /* outside of a line or block comment always starts a new comment.
#
# Finally, implicit newline characters can be deleted by block comments.
# Please see the examples below for details.
#
#
# After removing the comments from the source code, return the source code in
# the same format.
#
# Example 1:
#
# Input:
# source = ["/*Test program */", "int main()", "{ ", "  // variable declaration
# ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ",
# "   testing */", "a = b + c;", "}"]
#
# The line by line code is visualized as below:
# /*Test program */
# int main()
# {
# ⁠ // variable declaration
# int a, b, c;
# /* This is a test
# ⁠  multiline
# ⁠  comment for
# ⁠  testing */
# a = b + c;
# }
#
# Output: ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]
#
# The line by line code is visualized as below:
# int main()
# {
# ⁠
# int a, b, c;
# a = b + c;
# }
#
# Explanation:
# The string /* denotes a block comment, including line 1 and lines 6-9. The
# string // denotes line 4 as comments.
#
#
#
# Example 2:
#
# Input:
# source = ["a/*comment", "line", "more_comment*/b"]
# Output: ["ab"]
# Explanation: The original source string is
# "a/*comment\nline\nmore_comment*/b", where we have bolded the newline
# characters.  After deletion, the implicit newline characters are deleted,
# leaving the string "ab", which when delimited by newline characters becomes
# ["ab"].
#
#
#
# Note:
# The length of source is in the range [1, 100].
# The length of source[i] is in the range [0, 80].
# Every open block comment is eventually closed.
# There are no single-quote, double-quote, or control characters in the source
# code.
#
#
from typing import List
# @lc code=start


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        SINGLE_LINE_COMMENT = "//"
        MULTI_LINE_COMMENT_START = "/*"
        MULTI_LINE_COMMENT_END = "*/"
        # make a copy and reverse the list
        stack = source[:]
        stack.reverse()
        filtered = []
        while stack:
            line = stack.pop()
            # print(line)
            idx_single_line = line.find(SINGLE_LINE_COMMENT)
            idx_multi_start = line.find(MULTI_LINE_COMMENT_START)
            multi_line_comment_processing = False

            if idx_single_line == -1 and idx_multi_start == -1:
                # not an comment line
                filtered.append(line)
            elif idx_single_line != -1 and (idx_multi_start == -1 or idx_single_line < idx_multi_start):
                # single line comment
                filtered_line = line[:idx_single_line]
                if filtered_line:
                    filtered.append(filtered_line)
            elif idx_multi_start != -1 and (idx_single_line == -1 or idx_multi_start < idx_single_line):
                # multiple line comment
                idx_multi_end = line.find(
                    MULTI_LINE_COMMENT_END, idx_multi_start + 2)
                if idx_multi_end == -1:
                    filtered_line_start = line[:idx_multi_start]
                    multi_line_comment_processing = True
                else:
                    filtered_line_left = line[:idx_multi_start]
                    filtered_line_right = line[idx_multi_end + 2:]
                    filtered_line = filtered_line_left + filtered_line_right
                    if filtered_line:
                        stack.append(filtered_line)

            if not multi_line_comment_processing:
                continue

            while stack:
                line = stack.pop()
                idx_multi_end = line.find(MULTI_LINE_COMMENT_END)
                if idx_multi_end != -1:
                    filtered_line = filtered_line_start + \
                        line[idx_multi_end + 2:]
                    if filtered_line:
                        # filtered.append(filtered_line)
                        stack.append(filtered_line)
                    break

        return filtered


s = Solution()
source = ["//a", "b", "c //bala"]
source = ["a/*comment", "line", "more_comment*/b"]
source = ["a/*/b//*c","blank","d/*/e*//f"]
source = ["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"]
source = [
    "/*Test program */",
    "int main()",
    "{ ",
    "  // variable declaration",
    "int a, b, c;",
    "/* This is a test",
    "   multiline  ",
    "   comment for ",
    "   testing */",
    "a = b + c;",
    "}",
    ]
output = ["struct Node{","    ","    int size;","    int val;","};"]
output = ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]
# output = ["ae*"]
# print(s.removeComments(source))
# print(output)
# output: ["ab"]

# @lc code=end
