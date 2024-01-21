class Solution:
    def interpret(self, s: str) -> str:
        ss=''
        for i in range(len(s)):
            if s[i]=="(" and s[i+1]==")":
                ss+='o' 
            elif s[i]=='G':
                ss+='G'
            elif s[i]=='(' and s[i+1]=='a' and s[i+2]=='l' and s[i+3]==')':
                ss+="al"
        return ss