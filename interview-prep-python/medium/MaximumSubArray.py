class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [-5,-3,-1]
        """

        maxSum = nums[0]
        currSum = 0

        for num in nums:
            if currSum < 0:
                currSum = 0
            
            currSum += num
            
            maxSum = max(maxSum, currSum)


        return maxSum
