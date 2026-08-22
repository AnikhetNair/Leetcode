class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        k = sorted(s)
        n = sorted(t)
        
        for i in range(len(k)):
            if k[i] != n[i]:
                # Return the mismatched character from 'n' (string t)
                return n[i]
                
        # If no mismatch was found in the loop, the extra character is at the end
        return n[-1]
        