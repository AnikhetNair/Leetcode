class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        k=str(n)
        sm=0
        for i in range(len(k)):
            if i%2==0:
                sm+=int(k[i])
            else:
                sm-=int(k[i])
        return sm

        