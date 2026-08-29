class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        prev=0
        t=[]
        for k in nums:
            if k==prev:
                t.append(k)
            prev=k
        return t

        