class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        sorted_array = sorted(set(arr))

        rank_map = {value: rank + 1 for rank, value in enumerate(sorted_array)}

        return [rank_map[num] for num in arr]
    