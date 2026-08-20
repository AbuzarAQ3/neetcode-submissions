# unoptimized approach

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mx = Counter(nums).most_common(1)
        return mx[0][0]