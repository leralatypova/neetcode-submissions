class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen = defaultdict(int)
        for val in nums:
            seen[val] += 1 
        sort_seen = sorted(seen, key = seen.get, reverse = True)
        return sort_seen[:k]