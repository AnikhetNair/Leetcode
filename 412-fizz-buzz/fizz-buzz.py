class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        k=[]
        for i in range(1,n+1):
            if i%3==0:
                if i%5==0:
                    k.append("FizzBuzz")
                    continue
                k.append("Fizz")
            elif i%5==0:
                k.append("Buzz")
            else:
                k.append(str(i))
        return k
            

