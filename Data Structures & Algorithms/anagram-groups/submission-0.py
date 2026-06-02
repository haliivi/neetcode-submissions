class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for str_ in strs:
            count = [0] * 26
            for c in str_:
                diff = ord(c) - ord('a')
                count[diff] += 1
            res[tuple(count)].append(str_)
        return list(res.values())
