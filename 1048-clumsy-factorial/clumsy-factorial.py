class Solution(object):
    def clumsy(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Push the first number onto the stack
        stack = [n]
        
        # Operations rotation tracker: 0=*, 1=//, 2=+, 3=-
        op = 0 
        
        # Count down from n-1 to 1
        for i in range(n - 1, 0, -1):
            if op == 0:
                stack.append(stack.pop() * i)
            elif op == 1:
                # Use int() for truncation toward zero to handle negative division correctly
                stack.append(int(stack.pop() / float(i)))
            elif op == 2:
                stack.append(i)
            elif op == 3:
                stack.append(-i)
            
            # Move to the next operation in the 4-step rotation
            op = (op + 1) % 4
            
        return sum(stack)
