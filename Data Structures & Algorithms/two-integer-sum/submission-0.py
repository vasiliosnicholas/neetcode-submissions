class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {num:index for index, num in enumerate(nums)}
        for num_index, num in enumerate(nums):
            num_two = target - num
            if num_two in indices and num_index != indices[num_two]:
                answer = [num_index, indices[num_two]]
                answer.sort()
                return answer
        return [None, None]