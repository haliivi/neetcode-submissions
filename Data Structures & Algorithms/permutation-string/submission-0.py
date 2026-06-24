class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s_1_count, s_2_count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s_1_count[ord(s1[i]) - ord('a')] += 1
            s_2_count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if s_1_count[i] == s_2_count[i] else 0)
        
        l = 0

        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            index = ord(s2[r]) - ord('a')
            s_2_count[index] += 1
            if s_1_count[index] == s_2_count[index]:
                 matches += 1
            elif s_1_count[index] + 1 == s_2_count[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            s_2_count[index] -= 1
            if s_1_count[index] == s_2_count[index]:
                matches += 1
            elif s_1_count[index] - 1 == s_2_count[index]:
                matches -= 1
            l += 1
        return matches == 26

