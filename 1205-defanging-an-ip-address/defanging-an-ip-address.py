class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        k=[]
        for l in address:
            if l=='.':
                k.append('[.]')
            else : k.append(l)
        return "".join(k)
        