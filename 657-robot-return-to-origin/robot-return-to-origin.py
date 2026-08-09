class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x=0
        y=0
        for char in moves:
            if char=="U":
                y+=1
            if char=="D":
                y-=1
            if char=="L":
                x+=1
            if char=="R":
                x-=1
        return x==0 and y==0
        