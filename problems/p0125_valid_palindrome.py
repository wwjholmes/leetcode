"""LeetCode 125: Valid Palindrome."""

import logging

class Solution:
    logger = logging.getLogger(__name__)

    def isPalindrome(self, s: str) -> bool:
        """Return True if s is a palindrome, considering only alphanumeric
        characters and ignoring case; False otherwise.

        Constraints: 1 <= len(s) <= 1000; s contains only printable ASCII.
        """
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format=f"%(message)s")

    sol = Solution()

    # test case 1
    s = "Was it a car or a cat I saw?"
    assert sol.isPalindrome(s), f"{s} is plaindrome"

    # test case 2
    s = ""
    assert sol.isPalindrome(s), f"{s} is plaindrome"

    # test case 3
    s = " "
    assert sol.isPalindrome(s), f"{s} is plaindrome"

    # test case 4
    s = "?? !! "
    assert sol.isPalindrome(s), f"{s} is plaindrome"

    # test case 3
    s = "tab a cat"
    assert not sol.isPalindrome(s), f"{s} is not plaindrome"
