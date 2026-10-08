class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""
        
        base_word = strs[0]
        lcp = ""
        
        for i in range(len(base_word)):
            char_to_match = base_word[i]
            
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != char_to_match:
                    return lcp
            
            lcp += char_to_match
            
        return lcp
