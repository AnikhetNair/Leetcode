class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth=0
        r=0
        for k in s:
            if k==')':
                depth-=1
                continue
            if k!='(':
                continue
            depth+=1
            if depth>r:
                r=depth
        return r