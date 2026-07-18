class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indexed_nums = [(num, index) for index, num in enumerate(nums)]
        indexed_nums.sort()

        left_index = 0
        right_index = len(indexed_nums) - 1

        while left_index < right_index:

            current_sum = (
                indexed_nums[left_index][0]
                + indexed_nums[right_index][0]
            )

            if current_sum == target:
                return [
                    indexed_nums[left_index][1],
                    indexed_nums[right_index][1]
                ]

            elif current_sum < target:
                left_index += 1

            else:
                right_index -= 1
