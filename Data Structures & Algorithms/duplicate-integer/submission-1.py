class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # bruteforce
        # size = len(nums)
        # for i in range(size):
        #     for j in range(i+1, size):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # optiomal (hash map)
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
