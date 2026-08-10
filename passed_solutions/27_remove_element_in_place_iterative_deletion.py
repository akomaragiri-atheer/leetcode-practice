class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if not nums:
            return 0

        current_position = 0

        while current_position < len(nums):
            if nums[current_position] == val:
                del nums[current_position]
            else:
                current_position += 1
            
        return current_position
