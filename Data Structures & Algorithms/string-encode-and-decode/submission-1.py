class Solution:

    def encode(self, strs: List[str]) -> str:
        a =""
        for s in strs:
            count = len(s)
            a = str(a) + str(count) + "#" + s + "#"
        return a

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i<len(s):
            j = s.find("#",i)
            length = int(s[i:j])
            start_of_str = j + 1
            end_of_str = start_of_str + length
            actual_str = s[start_of_str:end_of_str]
            res.append(actual_str)
            i = end_of_str + 1
        return res
