class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        ds=sum(int(d) for d in str(num))
        return (num-(ds%2))//2
        