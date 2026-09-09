class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Already solved this on leetcode.
        #TODO: try with bucketsort
        num_freqs = defaultdict(int)
        for num in nums: #O(n)
            num_freqs[num] += 1
        freqs = [(-freq, num) for num, freq in num_freqs.items()]
        heapq.heapify(freqs) #O(n)
        return [heapq.heappop(freqs)[1] for _ in range(k)] #O(klog(n))