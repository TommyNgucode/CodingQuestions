class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        distinctSet = {}
        if len(nums) == len(set(nums)):
            return False

        for i in range(len(nums)): 
            if nums[i] in distinctSet: #checks key not value
                return True
            
            distinctSet[nums[i]] = i
        
        return False