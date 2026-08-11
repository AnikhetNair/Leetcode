class Solution(object):
    def canJump(self, nums):
        farthest = 0
        
        for i, jump in enumerate(nums):
            # If current index is beyond the maximum reach, we are stuck
            if i > farthest:
                return False
            
            # Update the maximum reachable index
            farthest = max(farthest, i + jump)
            
            # Early exit: if we can already reach the last index
            if farthest >= len(nums) - 1:
                return True
                
        return True