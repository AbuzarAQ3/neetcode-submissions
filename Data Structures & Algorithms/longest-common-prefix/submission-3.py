class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

    # bruteforce approach
        # if not strs:
        #     return ""
        
        # base_word = strs[0]
        # lcp = ""
        
        # for i in range(len(base_word)):
        #     char_to_match = base_word[i]
            
        #     for j in range(1, len(strs)):
        #         if i >= len(strs[j]) or strs[j][i] != char_to_match:
        #             return lcp
            
        #     lcp += char_to_match
            
        # return lcp

    # bruteforce but slightly optimized approach

        op = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return op
            op += strs[0][i]
        return op