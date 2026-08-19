class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        left=0
        k=list(s)
        right=len(k)-1
        if len(k)<=1:
            return s
        while left<=right:
            if k[left].isalpha() and k[right].isalpha():
                temp=k[left]
                k[left]=k[right]
                k[right]=temp
                left+=1
                right-=1
            if  not k[left].isalpha():
                left+=1
            if not k[right].isalpha():
                right-=1
        return "".join(k)

        
        