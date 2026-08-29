class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=1
        for k in nums:
            j*=k
        if j>0:
            return 1
        elif j==0:
            return 0
        else:
            return -1
        