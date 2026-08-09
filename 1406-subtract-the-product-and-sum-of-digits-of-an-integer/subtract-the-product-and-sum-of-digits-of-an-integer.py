class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        p=1
        k=n
        while k>0:
            p*=k%10
            k//=10
        k=n
        s=0
        while k>0:
            s+=k%10
            k//=10
        return p-s
        