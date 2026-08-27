class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        k=(high-low)//2
        if high%2!=0 or low%2!=0:
            k+=1
        return k
        