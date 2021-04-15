#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (30.49%)
# Likes:    9975
# Dislikes: 661
# Total Accepted:    1.2M
# Total Submissions: 4M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
# 
# 
# Example 1:
# 
# 
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: s = "cbbd"
# Output: "bb"
# 
# 
# Example 3:
# 
# 
# Input: s = "a"
# Output: "a"
# 
# 
# Example 4:
# 
# 
# Input: s = "ac"
# Output: "a"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consist of only digits and English letters (lower-case and/or upper-case),
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #P(i, j) = P(i+1, j-1) and s[i] == s[j]
        # base case 
        # 1) P(i, i) = 1
        # 2) P(i, i+1) = 1 if s[i] == s[i+1]
        length = len(s)
        p = [[None for j in range(length)] for i in range(length)]
        longest = ""

        # base case substring size == 1
        for i in range(length):
            p[i][i] = True
            longest = s[i] if p[i][i] else longest

        # base cae substring size == 2
        for i in range(length-1):
            p[i][i+1] = True if s[i] == s[i+1] else False
            longest = s[i:i+2] if p[i][i+1] else longest

            
        for size in range(3, length + 1):
            for i in range(length - size + 1):
                j = i + size - 1
                p[i][j] = True if p[i+1][j-1] and s[i] == s[j] else False
                if p[i][j] and len(longest) < size:
                    longest = s[i:j+1]
        return longest

# sol = Solution()
# s = "babad"
# s = "cbbd"
# s = "jaliztdispcppzgzjxnjxwbhhtbjrijyibqwrhwuscmokylygielwssuyretqnoiglvsltmhetvdoliwibrnwmdtauczcswuqxxokaykslfzgxovphdptgtrbbozdkdgawcegemkumgbyqzjrzurkdaibfwwvcxfcstvixisrcfxvnlzizlbnacxssetlsxrvcaqvzmbnzdfmtskmxmjblzgpdsjvhqhrihiajvwxbmjsncjhmilercbdbzyncrnlyrxrefaeuttkscfttqnedzvqisclbremuxmngrpgqjqkijpizkixkrgaarpknivrrirbkeddkulvlfuetbdnugzodbfufqhrpkyufhrhnnnzsenkvqsuhlbaimniusuxsnmavqbilzgsfxjykrxdkkpnneikwlucdghnikojythrpgwyzoqgraycavrivsbfuaonssmryhcykooivrxmeeowllsfeyxrznvkdpobohpzolnpbxjjxbpnlozphobopdkvnzrxyefsllwoeemxrviookychyrmssnoaufbsvirvacyargqozywgprhtyjokinhgdculwkiennpkkdxrkyjxfsgzlibqvamnsxusuinmiablhusqvknesznnnhrhfuykprhqfufbdozgundbteuflvlukddekbrirrvinkpraagrkxikzipjikqjqgprgnmxumerblcsiqvzdenqttfcskttueaferxrylnrcnyzbdbcrelimhjcnsjmbxwvjaihirhqhvjsdpgzlbjmxmkstmfdznbmzvqacvrxsltessxcanblzizlnvxfcrsixivtscfxcvwwfbiadkruzrjzqybgmukmegecwagdkdzobbrtgtpdhpvoxgzflskyakoxxquwsczcuatdmwnrbiwilodvtehmtlsvlgionqteryusswleigylykomcsuwhrwqbiyjirjbthhbwxjnxjzgzppcpsidtzilaj"
# print(sol.longestPalindrome(s))

# @lc code=end
