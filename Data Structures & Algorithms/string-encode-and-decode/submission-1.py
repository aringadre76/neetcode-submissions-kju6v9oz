class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for str in strs:
            res += str + "~"
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        curr = ""
        for char in s:
            
            if char != "~":
                curr += char
            else:
                res.append(curr)
                curr = ""
        return res