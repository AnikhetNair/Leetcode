class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        v1=max(nums)-k
        v2=min(nums)+k 
        if v2>v1:
            v1+=v2-v1
        return abs(v1-v2)       