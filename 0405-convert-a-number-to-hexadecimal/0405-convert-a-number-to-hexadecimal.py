class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        if num < 0:
            num = 2**32 + num

        hex_digits = "0123456789abcdef"
        hex_str = ""

        while num > 0:
            hex_str += hex_digits[num % 16]
            num //= 16

        return hex_str[::-1]