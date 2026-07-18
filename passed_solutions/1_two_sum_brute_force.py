class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for first_index in range(len(nums)):
            for second_index in range(first_index + 1, len(nums)):
                if nums[first_index] + nums[second_index] == target:
                    return [first_index, second_index]
