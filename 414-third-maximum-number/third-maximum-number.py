class Solution(object):

  def thirdMax(self, nums):
    # Remove duplicates first, then sort
    unique_nums = sorted(list(set(nums)))

    # If fewer than 3 distinct numbers, return the maximum (last element)
    if len(unique_nums) < 3:
      return unique_nums[-1]

    # Return the 3rd maximum element
    return unique_nums[-3]