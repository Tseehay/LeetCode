class Solution:
    def smallestNumber(self, num: int) -> int:
#         310 301 013 031 103 130
        if num > 0:
            digits = sorted(str(num))
            if digits[0] == '0':
                for i in range(1, len(digits)):
                    if digits[i] != '0':
                        digits[0], digits[i] = digits[i], '0'
                        break
            return int(''.join(digits))
        else:
            digits = sorted(str(abs(num)), reverse=True)
            return int('-' + ''.join(digits))
            