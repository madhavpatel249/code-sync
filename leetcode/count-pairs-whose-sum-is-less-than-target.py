class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
    
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        count = 0

        left = 0
        right = len(nums)-1

        while left<right:
            sum=nums[left]+nums[right]
            if sum<target:
                count += right-left
                left += 1  
            else:
                right -=1

        return count