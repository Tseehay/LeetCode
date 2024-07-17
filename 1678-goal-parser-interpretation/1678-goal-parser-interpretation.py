class Solution:
    def interpret(self, s: str) -> str:
        res=""
        for i in range(len(command)):
            if command[i:i+2]=="()":
                res+="o"
            elif command[i:i+4]=="(al)":
                res+="al"
            elif command[i]=="G":
                res+="G"
        return res
