class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_val = min(nums)
        max_val = max(nums)
        
     
        return max(0, max_val - min_val - 2 * k)      