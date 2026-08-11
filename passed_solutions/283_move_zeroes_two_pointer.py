class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        kept = 0

        for pos in range(len(nums)):
            if nums[pos] != 0:
                nums[kept] = nums[pos]
                kept += 1
        for i in range(kept, len(nums)):
            nums[i] = 0
