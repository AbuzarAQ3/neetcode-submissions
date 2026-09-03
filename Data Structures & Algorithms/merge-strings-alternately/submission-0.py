class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        max_s = max(n, m)
        s = ''
        
        for i in range(max_s):
            try:
                if word1[i]:
                    s += word1[i]
            except IndexError:
                pass
            try:
                if word2[i]:
                    s += word2[i]
            except IndexError:
                pass

        return s