class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashMap = {}
        # for i in strs:
        #     sorted_key = "".join(sorted(i))
        #     if sorted_key not in hashMap:
        #         hashMap[sorted_key] = []
        #     hashMap[sorted_key].append(i)
        # return list(hashMap.values())
             
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord("a")] += 1
            res [tuple(count)].append(s)
        return list(res.values())
            
