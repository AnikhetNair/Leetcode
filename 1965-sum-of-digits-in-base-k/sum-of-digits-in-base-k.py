class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        sm=0
        while n>0:
            sm+=n%k
            n//=k
        return sm
        