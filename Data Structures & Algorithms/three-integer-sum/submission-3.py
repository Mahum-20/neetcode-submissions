class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        hashset = set()
        res = []
        for i, n in enumerate(nums):
            if n in hashset:
                continue
            else:
                hashset.add(n)
            l,r = i+1,len(nums)-1
            while l < r:
                if n+nums[l]+nums[r] < 0:
                    l+=1
                elif n+nums[l]+nums[r] > 0:
                    r-=1
                else:
                    res.append([n,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        return res
        