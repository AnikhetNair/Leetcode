class Solution(object):
    def distanceTraveled(self, a, b):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """
        return (a+min((a-1)//4,b))*10
        