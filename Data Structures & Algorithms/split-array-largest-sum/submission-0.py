class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(m: int) -> bool:
            subarray = 0
            cur_sum = 0
            for n in nums:
                cur_sum += n
                if cur_sum > m:
                    subarray += 1
                    cur_sum = n
            return subarray + 1 <= k

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            m = l + r >> 1
            if can_split(m):
                r = m - 1
                res = m
            else:
                l = m + 1
        return res