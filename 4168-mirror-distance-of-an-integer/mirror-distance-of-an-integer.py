class Solution(object):
    
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        k=str(n)
        k=k[::-1]
        k=int(k)
        return abs(n-k)
        