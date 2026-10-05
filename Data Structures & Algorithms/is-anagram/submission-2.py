class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

    # optimized hashmap approach
        # validate using length filter early on
        if len(s) != len(t):
            return False

        # create dict1 for s
        all_chars = dict()
        for char in s:
            if char in all_chars:
                all_chars[char] += 1
            else:
                all_chars[char] = 1

        #  create dict2 for t
        all_chars2 = dict()
        for char in t:
            if char in all_chars2:
                all_chars2[char] += 1
            else:
                all_chars2[char] = 1

        # compare dict1 and dict2
        if all_chars != all_chars2:
            return False
        return True