class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        k="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ret=""
        while columnNumber>0:
            columnNumber-=1
            ret=k[columnNumber%26]+ret
            columnNumber//=26
        return ret
        