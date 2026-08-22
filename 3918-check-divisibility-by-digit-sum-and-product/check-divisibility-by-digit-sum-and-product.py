class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sm=0
        pro=1
        k=n
        while n>=1:
            sm+=n%10
            pro*=n%10
            n//=10
        return k%(sm+pro)==0

        