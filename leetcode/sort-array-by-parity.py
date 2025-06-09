class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        

        array = []

        for i in range(len(nums)):
            if nums[i]%2 == 0:
                array.insert(0,nums[i])
            else:
                array.append(nums[i])

        return array