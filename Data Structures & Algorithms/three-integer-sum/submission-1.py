class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set[tuple[int, ...]]()
        nums.sort()
        for index, num in enumerate(nums):
            i = index + 1
            j = len(nums) - 1
            while i < j:
                sum = num + nums[i] + nums[j]
                if sum == 0:
                    t = [num, nums[i], nums[j]]
                    t.sort()
                    triplets.add(tuple(t))
                    j = j - 1 if j - 1 != index else j - 2
                    i = i + 1 if i + 1 != index else i + 2
                elif sum > 0:
                    j = j - 1 if j - 1 != index else j - 2
                elif sum < 0:
                    i = i + 1 if i + 1 != index else i + 2
                
        return [list(t) for t in triplets]
