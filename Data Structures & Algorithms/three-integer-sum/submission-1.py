# leetcode 15
# bruteforce
# TC: O(n^3)
# MC: O(1) or O(n)
#  class Solution:
#      def threeSum(self, nums: List[int]) -> List[List[int]]:
#         arr = []
#         n = len(nums)
#         nums.sort()
#         for i in range(n):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             for j in range(i+1, n):
#                 if j > i+1 and nums[j] == nums[j-1]:
#                     continue
#                 for k in range(j+1, n):
#                     if k > j+1 and nums[k] == nums[k-1]:
#                         continue
#                     if (nums[k] + nums[j] + nums[i]) == 0:
#                         arr.append([nums[i], nums[j], nums[k]])
#         return arr

# two pointers
# TC: O(n log n)(n^2) = O(n^2)
# MC: O(1) or O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            while l<r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    arr.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return arr


