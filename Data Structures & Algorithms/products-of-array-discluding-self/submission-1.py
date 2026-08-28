# unoptimized, bruteforce approach:
# 0% ai used.

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = (len(nums))
#         arr = []
#         prod = 1
#         for i in range(n):
#             for j in range(n):
#                 if j == i:
#                     continue
#                 prod = prod*nums[j]
#             arr.append(prod)
#             prod = 1
#         return arr

# optimzed two pointer approach:
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        op_arr = [1] * n

        prefix = 1
        for i in range(n):
            op_arr[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n-1, -1, -1):
            op_arr[i] *= postfix
            postfix *= nums[i]

        return op_arr








