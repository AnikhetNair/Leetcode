class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        gcount=len(g)-1
        scount=len(s)-1
        flag=0
        while gcount>=0 and scount>=0:
            if s[scount]>=g[gcount]:
                flag+=1
                scount-=1
                gcount-=1
            elif g[gcount]>s[scount]:
                gcount-=1
        return flag

        