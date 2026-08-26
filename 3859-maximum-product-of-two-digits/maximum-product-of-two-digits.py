class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        k=[]
        while n>0:
            k.append(n%10)
            n//=10
        k.sort()
        return k[-1]*k[-2]
        