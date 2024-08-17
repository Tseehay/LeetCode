class Solution:
    def sortSentence(self, s: str) -> str:
        arr = []
        for word in s.split():
            new = word[-1] + word[:-1]
            arr.append(new)
        arr.sort()
        ans = ""
        for i in arr:
            ans += i[1:] + ' '
        
        return ans[:-1]