class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=[]
        if len(nums)<2:
            return 0
        nums.sort()
        diff=0
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>diff:
                diff=nums[i]-nums[i-1]
        return diff
        