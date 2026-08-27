class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        relist = []
        for i in nums:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        value_list = list(res.values())
        value_list = sorted(value_list)
        for j in range(k):
            max_value = max(res, key=res.__getitem__)
            relist.append(max_value)
            res.pop(max_value)
        return relist


