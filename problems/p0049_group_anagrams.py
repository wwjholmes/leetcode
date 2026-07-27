"""LeetCode 49: Group Anagrams."""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        1. I plan to sort these str and use the sorted str as 'key', then add the 'str' to the list
        2. Then we iterate the dict and convert it to list[list[str]]

        """
        dict_ = {}
        for original in strs:
            sorted_str = ''.join(sorted(original))
            list_str = dict_.get(sorted_str, [])
            list_str.append(original)
            dict_[sorted_str] = list_str

        return list(sorted(dict_.values()))

if __name__ == "__main__":
    strs = ["act","pots","tops","cat","stop","hat"]
    output = [["hat"],["act", "cat"],["stop", "pots", "tops"]]
    s = Solution()

    actual = s.groupAnagrams(strs)
    assert sorted(map(sorted, actual)) == sorted(map(sorted, output)), f"expct {output}, but actual is {actual}"
