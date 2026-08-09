class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        n=num
        if n == 0:
            return "0"
        hex_digits = "0123456"
        result = ""
        
        n=abs(num)
        while n > 0:
            remainder = n % 7
            result = hex_digits[remainder] + result
            n //= 7
        if num<0:
            result='-'+result
        return result
        