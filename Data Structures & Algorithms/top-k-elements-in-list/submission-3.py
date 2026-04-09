class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        
        count = Counter(nums)
        
        # Create buckets: index = frequency
        bucket = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            bucket[freq].append(num)
        
        result = []
        
        # Traverse buckets from high frequency to low
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result