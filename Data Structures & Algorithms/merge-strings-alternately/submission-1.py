# approach A, ugly, bruteforce
# make it work first, optimize later

# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
        # n = len(word1)
        # m = len(word2)
        # max_s = max(n, m)
        # s = ''
        
        # for i in range(max_s):
        #     try:
        #         if word1[i]:
        #             s += word1[i]
        #     except IndexError:
        #         pass
        #     try:
        #         if word2[i]:
        #             s += word2[i]
        #     except IndexError:
        #         pass

        # return s

# optimised, beautified approach B, two pointer approach

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i = 0
        j = 0
        
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
            
        res.append(word1[i:])
        res.append(word2[j:])
        
        return "".join(res)