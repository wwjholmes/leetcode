"""LeetCode 271: Encode and Decode Strings."""


class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encode a list of strings into a single string."""
        # I will concatenate the string with the foramt
        # len(str1)#str1|len(str2)#str2|....
        formatted_strs = []
        for s in strs:
            length = len(s)
            formatted_strs.append(f"{length}#{s}")
        return "".join(formatted_strs)

    def decode(self, s: str) -> list[str]:
        """Decode a string produced by ``encode`` into the original strings."""
        s_right = s
        original_strs = []
        while s_right:
            index = s_right.find("#")
            length = int(s_right[:index])
            start = index + 1
            end = index + 1 + length
            sub_string = s_right[start:end]
            original_strs.append(sub_string)
            s_right = s_right[end:]

        return original_strs


if __name__ == "__main__":
    s = Solution()

    # test 1
    strs = ["abcd", "", "123"]
    encoded = s.encode(strs)
    print(f"encoded:{encoded}")
    decoded = s.decode(encoded)
    print(f"decoded:{decoded}")

    # test 2 
    strs = ["ab##d", "#", "123#"]
    encoded = s.encode(strs)
    print(f"encoded:{encoded}")
    decoded = s.decode(encoded)
    print(f"decoded:{decoded}")

    # test 3 
    strs = ["#abcd", "////", "123?"]
    encoded = s.encode(strs)
    print(f"encoded:{encoded}")
    decoded = s.decode(encoded)
    print(f"decoded:{decoded}")

    # test 4 
    strs = ["", ""]
    encoded = s.encode(strs)
    print(f"encoded:{encoded}")
    decoded = s.decode(encoded)
    print(f"decoded:{decoded}")

    # test 5 
    strs = []
    encoded = s.encode(strs)
    print(f"encoded:{encoded}")
    decoded = s.decode(encoded)
    print(f"decoded:{decoded}")