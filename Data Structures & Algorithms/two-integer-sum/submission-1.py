class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # bruteforcce 
        # T O(n^2)
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
    # optimized hashmap approach
        # T O(n)
        hash_map = dict()
        for i, num in enumerate(nums):
            hash_map[num] = i
            
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in hash_map and hash_map[complement] != i:
                return [i, hash_map[complement]]
                
        return []