class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i, l, r = 0, 0, len(nums) - 1

        def swap(j, k):
            nums[j], nums[k] = nums[k], nums[j]

        while i <= r:
            if nums[i] == 0:
                swap(i, l)
                l += 1
            elif nums[i] == 2:
                swap(r, i)
                r -= 1
                i -= 1
            i += 1