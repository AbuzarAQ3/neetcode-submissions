class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
        
        cand1, cand2 = 0, 1
        cnt1, cnt2 = 0, 0
        
        for num in nums:
            if num == cand1:
                cnt1 += 1
            elif num == cand2:
                cnt2 += 1
            elif cnt1 == 0:
                cand1, cnt1 = num, 1
            elif cnt2 == 0:
                cand2, cnt2 = num, 1
            else:
                cnt1 -= 1
                cnt2 -= 1
                
        result = []
        threshold = len(nums) // 3
        
        if nums.count(cand1) > threshold:
            result.append(cand1)
        if cand1 != cand2 and nums.count(cand2) > threshold:
            result.append(cand2)
            
        return result
