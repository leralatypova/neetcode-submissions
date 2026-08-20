class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for val in strs:
            s = ''.join(sorted(val))
            seen[s].append(val)
        return list(seen.values())