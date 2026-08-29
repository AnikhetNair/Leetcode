class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        squared = sorted([x * x for x in nums], reverse=True)
        n = len(nums)
        pos_count = (n + 1) // 2
        return sum(squared[:pos_count]) - sum(squared[pos_count:])
        