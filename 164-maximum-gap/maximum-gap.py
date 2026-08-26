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
        for i in range(1,len(nums)):
            k.append(abs(nums[i]-nums[i-1]))
        k.sort()
        return k[-1]
        