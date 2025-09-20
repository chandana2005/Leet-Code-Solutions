class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res= defaultdict(list)
        for i in strs:
            Sorteds= ''.join(sorted(i))
            res[Sorteds].append(i)
        return list(res.values())
