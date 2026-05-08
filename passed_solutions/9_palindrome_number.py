class StringConversionSolution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


class TwoPointerSolution:
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


class MathematicalSolution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original_number = x
        reversed_number = 0

        while x > 0:
            last_digit = x % 10

            reversed_number = (reversed_number * 10) + last_digit

            x = x // 10

        return original_number == reversed_number
