from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        window_count = Counter()
        
        k = len(s1)
        
        for i in range(k):
            window_count[s2[i]] += 1
            
        if s1_count == window_count:
            return True
            
        for i in range(k, len(s2)):
            window_count[s2[i]] += 1
            
            left_char = s2[i - k]
            window_count[left_char] -= 1
            
            if window_count[left_char] == 0:
                del window_count[left_char]
                
            if s1_count == window_count:
                return True
                
        return False
