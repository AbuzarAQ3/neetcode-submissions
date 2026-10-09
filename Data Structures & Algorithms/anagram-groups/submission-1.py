class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # sorted string for key approach
        # T O(n*m*log*m)
        # S O(n*m)

        anagrams = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            anagrams[key].append(word)
        
        return list(anagrams.values())