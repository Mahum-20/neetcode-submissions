class Solution:
    def isValid(self, s: str) -> bool:
        hashlist = []
        for c in s:
            if c == "[" or c == "{" or c == "(":
                hashlist.append(c)
            else:
                if not hashlist:
                    return False
                x = hashlist[-1]
                if (c == "]" and x == "[") or \
                    (c == "}" and x == "{") or \
                    (c == ")" and x == "("):
                    hashlist.pop()
                else:
                    return False
        return True if not hashlist else False