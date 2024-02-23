class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        descending_order_heights = sorted(heights, reverse = True)

        result = []

        for i in range(len(names)):
            curr_largest_index = heights.index(descending_order_heights[i])
            result.append(names[curr_largest_index])

        return result
