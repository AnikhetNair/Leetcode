class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sm=0
        c=0
        for i in (nums):
            if i%6==0:
                sm+=i
                c+=1
        if c==0:
            return 0
        return sm//c
        