class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        #  bruteforce approach
        # n = len(nums)
        # ans = [0]*2*n
        # for i in range(n):
        #     ans[i] = nums[i]
        # for i in range(n, 2*n):
        #     ans[i] = nums[i-n]
        # return ans

        # singular loop approach, optimized bruteforce
        size = len(nums)
        c = 0
        new_arr = [0]*(2*size)
        for i in range(size*2):
            if i < size:
                new_arr[i] = nums[i]
            if i >= size:
                new_arr[i] = nums[c]
                c+=1
        return new_arr