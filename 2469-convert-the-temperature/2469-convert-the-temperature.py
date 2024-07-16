class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        l=[]
        ke = celsius + 273.15
        fa = celsius * 1.80 + 32.00
        l.append(ke)
        l.append(fa)
        return l