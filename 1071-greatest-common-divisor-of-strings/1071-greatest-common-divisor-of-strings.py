class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        # Find the minimum length between str1 and str2
        min_len = min(len1, len2)

        # Starting from the minimum length, check if the substring divides both str1 and str2
        for i in range(min_len, 0, -1):
            if len1 % i == 0 and len2 % i == 0:
                divisor = str1[:i]

                # Check if the divisor divides both str1 and str2
                if str1 == divisor * (len1 // i) and str2 == divisor * (len2 // i):
                    return divisor

        return ""