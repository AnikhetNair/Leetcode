class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        for j in range(len(nums)):
            a.append(nums[nums[j]])
        return a
        