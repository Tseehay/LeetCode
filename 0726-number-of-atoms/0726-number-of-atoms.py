class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        i = 0
        stack = [{}]

        while i < n:
            if formula[i] == '(':
                stack.append({})
                i += 1
            elif formula[i] == ')':
                i += 1
                num_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                factor = int(formula[num_start:i] or 1)
                top = stack.pop()
                for elem, freq in top.items():
                    if elem in stack[-1]:
                        stack[-1][elem] += freq * factor
                    else:
                        stack[-1][elem] = freq * factor
            else:
                elem_start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                elem = formula[elem_start:i]
                num_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                num = int(formula[num_start:i] or 1)
                if elem in stack[-1]:
                    stack[-1][elem] += num
                else:
                    stack[-1][elem] = num

        count = stack.pop()
        ans = ""
        for elem in sorted(count.keys()):
            ans += elem
            if count[elem] > 1:
                ans += str(count[elem])

        return ans