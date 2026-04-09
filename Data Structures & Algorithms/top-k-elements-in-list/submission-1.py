class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        
        count = Counter(nums)  # {num: frequency}
        
        # Sort by frequency (descending)
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        
        # Take top k elements
        return [num for num, freq in sorted_items[:k]]