class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        left1, left2 = 0, 0 # initialize two pointers at both arrays

        while left1 < len(nums1) and left2 < len(nums2):
            if nums1[left1] == nums2[left2]: # if the same, return
                return nums1[left1]

            if nums1[left1] < nums2[left2]: # increment whichever is smaller, since increasing order
                left1 += 1
            else:
                left2 += 1


        return -1 # if not found, return - 1
