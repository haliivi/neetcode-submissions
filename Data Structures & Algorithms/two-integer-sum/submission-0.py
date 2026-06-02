class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevHashMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevHashMap:
                return [prevHashMap[diff], i]
            prevHashMap[n] = i