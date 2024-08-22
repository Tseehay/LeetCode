class Solution:
    def findComplement(self, num: int) -> int:
        bit = 0
        todo = num
        while todo:
            bit = bit << 1
            bit = bit ^ 1
            todo = todo >> 1
        return bit ^ num