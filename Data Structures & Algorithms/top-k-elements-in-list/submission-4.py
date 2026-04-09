class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        
        count = Counter(nums)
        
        # Get k largest by frequency
        return [num for num, _ in heapq.nlargest(k, count.items(), key=lambda x: x[1])]