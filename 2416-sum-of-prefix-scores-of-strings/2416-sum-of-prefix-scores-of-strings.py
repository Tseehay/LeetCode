class Trie:
    def __init__(self):
        self.ch = [None] * 26
        self.visited = 0
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie, a, ans = Trie(), ord('a'), []
        for x in words:
            t = trie
            for c in x:
                c = ord(c) - a
                if not t.ch[c]: t.ch[c] = Trie()
                t.ch[c].visited += 1
                t = t.ch[c]
        for x in words:
            t, curr = trie, 0
            for c in x:
                c = ord(c) - a
                curr += t.ch[c].visited
                t = t.ch[c]
            ans.append(curr)
        return ans