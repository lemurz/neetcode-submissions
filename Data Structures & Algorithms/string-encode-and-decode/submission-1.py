class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        count = 0

        if strs is None:
            return out

        for string in strs:
            out += str(len(string)) + "#" + string 

        return out

    def decode(self, s: str) -> List[str]:
        out, i = [], 0

        if s=="":
            return out

        while i < len(s):
            j = i
            string = ""

            while s[j] != "#":
                j+=1 
            length = int(s[i:j])

            string += (s[j+1 : j+1+length])
            out.append(string)

            i = j + 1 + length
        
        print(out)

        return out
            






