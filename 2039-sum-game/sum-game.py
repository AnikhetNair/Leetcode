class Solution:
    def sumGame(self, num):
        n = len(num)
        mid = n // 2
        
        sum_diff = 0  # S_left - S_right
        q_diff = 0    # Q_left - Q_right
        
        for i in range(mid):
            if num[i] == '?':
                q_diff += 1
            else:
                sum_diff += int(num[i])
                
        for i in range(mid, n):
            if num[i] == '?':
                q_diff -= 1
            else:
                sum_diff -= int(num[i])
        
        # If total question marks is odd, Alice always wins.
        # Otherwise, check if Bob can force equality via the 9-complement strategy.
        return sum_diff * 2 + q_diff * 9 != 0