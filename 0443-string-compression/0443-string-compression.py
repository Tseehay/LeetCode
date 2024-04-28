class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        i = 0

        while i < len(chars):
            char = chars[i]
            count = 0
            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1
            chars[index] = char
            index += 1
            if count > 1:
                for digit in str(count):
                    chars[index] = digit
                    index += 1

        return index
