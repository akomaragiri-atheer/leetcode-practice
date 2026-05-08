class Solution:
    def isPalindrome(self, x: int) -> bool:
        number_as_string = str(x)

        left_index = 0
        right_index = len(number_as_string) - 1

        while left_index < right_index:
            if number_as_string[left_index] != number_as_string[right_index]:
                return False

            left_index += 1
            right_index -= 1

        return True
