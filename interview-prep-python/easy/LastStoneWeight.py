class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        # we negate everything because heapq.heapify() creates a min heap
        stones = [-s for s in stones] 
        heapq.heapify(stones)

        while len(stones) > 1:
            first, second = heapq.heappop(stones), heapq.heappop(stones)
            #e.g. -6, -2

            if first < second: # there could be a tie
                heapq.heappush(stones, -(-first - (-second)))
        
        if len(stones) > 0:
            return -stones[0]
        else:
            return 0 
        
