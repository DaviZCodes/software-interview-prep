class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        e.g. [10,9,2,5,3,7,101,18]
        '''

        LIS = [1] * len(nums) # [1,1,1,1,1,1,1,1]

        for i in range(len(nums) - 1, -1, -1): 
            # start with the last index, iterating backwards
            for j in range(i + 1, len(nums)): 
                # compare with all the indices after j
                if nums[i] < nums[j]: # it is increasing order
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)


        
