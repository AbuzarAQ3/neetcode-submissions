class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # bruteforce approach
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
            
        # optimized approach, hashmap
        # set_of_elements = set()
        # for num in nums:
        #     if num in set_of_elements:
        #         return True
        #     set_of_elements.add(num)
        # return False

        # optimized trick approach
        return len(nums) != len(set(nums))