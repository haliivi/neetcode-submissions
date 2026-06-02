class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0
        for num in nums:
            if count == 0:
                res = num
            count += (1 if res == num else -1)
        return res

        # count = {}
        # res, maxCount = 0, 0
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        #     res = num if count[num] > maxCount else res
        #     maxCount = max(count[num], maxCount)
        # return res