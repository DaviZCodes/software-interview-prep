# House Robber 1 - Leetcode 198

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            '''
            e.g [rob1, rob2, n, n + 1]
            for the temp, we can include n + rob1, we must include
            both because this provides a greater value.

            For rob2, we cannot include n because it's right next to it.
            '''
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2
