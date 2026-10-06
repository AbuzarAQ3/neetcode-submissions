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
        for i, element in enumerate(nums):
            hash_map[element] = i
            
        for i, element in enumerate(nums):
            solution = target - element
            if solution in hash_map and hash_map[solution] != i:
                return [i, hash_map[solution]]