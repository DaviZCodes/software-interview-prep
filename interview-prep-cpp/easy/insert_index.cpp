/*
File: Find Array's Insert Index
Author: DaviZCodes
Question (easy): 
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
*/

//algorithm in O(log n) means I must use some kind of sort algoritm with a left pointer, right pointer, and mid_index

int findInsertIndex(vector<int> nums, const int target){
  #setting left and right pointers
  int left_pointer = 0;
  int right_pointer = nums.size() - 1;
  
  while (left_pointer < right_pointer){
    //setting mid_index
    int middle_index = (left_pointer + right_pointer)/2;
    
    //if found, return the index
    if (nums[middle_index] == target){
      return middle_index;
    }
    
    //if target is smaller, right pointer decreases
    else if (nums[middle_index] > target){
      right_pointer = middle_index - 1;
    }
    
    //if target is greater, left pointer increases
    else if (nums[middle_index] < target){
      left_pointer = middle_index + 1; 
    }
  }
  
  //this is useful in case the target is not in the array
  //let's say an array [1,2,3] and the target is 0, then the number 0 would be placed in the 0 index
  if (nums[left_pointer] >= target){
    return left_pointer;
  }
  
  //the index position would be its position + 1 
  else {
    return left_pointer + 1;
  }
}
