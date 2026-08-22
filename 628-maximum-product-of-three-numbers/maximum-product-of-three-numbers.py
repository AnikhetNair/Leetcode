class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        k=nums[-1]*nums[-2]*nums[-3]
        t=nums[0]*nums[1]*nums[-1]
        return max(k,t)
        