class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=sum(nums)
        t=sum(set(nums))
        n=len(nums)//2
        return (k-t)/(n-1)
        