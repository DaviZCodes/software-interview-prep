
"""
217. Contains Duplicate 
  Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
  
class Solution(object):
  def containsDuplicate(self, nums):
      """
      :type nums: List[int]
      :rtype: bool
      """
      #set solution runtime: o(n) memory: o(n)
      num_set = set()

      for num in nums:
          if num in num_set:
              return True
          num_set.add(num)
      
      return False

      """
      #sort solution, runtime: o(nlogn) memory: o(1) 
      nums.sort()

      for i in range(len(nums)):
          if nums[i] == nums[i+1]:
              return True

      return False
      """
