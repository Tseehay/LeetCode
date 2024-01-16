class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        wr=s.split()
        wr.reverse()
        rev=' '.join(wr)
        return rev
            