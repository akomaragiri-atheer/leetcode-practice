class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if not nums:
            return 0

        next_position = 0

        for current_position in range(len(nums)):
            if nums[current_position] != val:
                nums[next_position] = nums[current_position]
                next_position += 1

        return next_position
