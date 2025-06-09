class Solution:
    def findMaxK(self, nums):
        nums.sort()
        left, right = 0, len(nums) - 1
        
        while left < right:
            total = nums[left] + nums[right]
            if total == 0:
                return nums[right]
            elif total > 0:
                right -= 1
            else:
                left += 1
        
        return -1