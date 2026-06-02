class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for i in range(len(strs[0])):
            for str_ in strs:
                if i == len(str_) or str_[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res