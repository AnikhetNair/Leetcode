class Solution(object):
    def minSensors(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        row=(m+2*k)//(2*k+1)
        col=(n+2*k)//(2*k+1)
        return row*col