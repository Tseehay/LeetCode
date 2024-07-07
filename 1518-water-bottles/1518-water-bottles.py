class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        s = 0

        while numBottles >= numExchange:
            K = numBottles // numExchange
            s += numExchange * K
            numBottles -= numExchange * K
            numBottles += K

        return s + numBottles
            