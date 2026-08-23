class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        count=0
        left=0
        right=len(nums)-1
        while left<right:
            if nums[left]+nums[right]<k:
                left+=1
            elif nums[left]+nums[right]>k:
                right-=1
            else:
                left+=1
                right-=1
                count+=1
        return count
        