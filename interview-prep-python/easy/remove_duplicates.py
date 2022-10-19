'''
File: Remove Duplicates 
Author: DaviZCodes
Question:
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.

nums is a list of integers in ascending order. Return the length of the new list without duplicates. 
'''

def remove_duplicates(nums):
  left_pointer = 1

  #start at 1 because val at index 0 is definitely not a duplicate. It stays where it is. 
  for i in range(1, nums):
    #if the value is unique, in other words, if the value is not equal to the previous one
    if nums[i] != nums[i - 1]:
      #the new list will have a unique value
      nums[left_pointer] = nums[i]
      #increment the left pointer by one once a unique value is found
      left_pointer += 1
    
  #we return left_pointer because the left pointer shows the index of the final value of the list with unique values
  return left_pointer
