class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        s=start
        for i in range(1,n):
            s=s^(start+2*i)
        return s
        