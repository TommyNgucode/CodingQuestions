class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        duplicates = {}

        for i in range(len(nums)):
            if nums[i] in duplicates:
                storedNum = duplicates[nums[i]] 
                if (i - storedNum) <= k:
                    return True

            duplicates[nums[i]] = i

        return False