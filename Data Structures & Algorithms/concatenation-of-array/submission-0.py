class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
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