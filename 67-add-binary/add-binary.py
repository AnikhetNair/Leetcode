class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        k=int(a,2)
        l=int(b,2)
        s=k+l
        return "{0:b}".format(s)
        