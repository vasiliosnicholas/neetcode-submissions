class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freqs = defaultdict(int)
        for num in nums:
            num_freqs[num] += 1
        freqs = [(-freq, num) for num, freq in num_freqs.items()]
        heapq.heapify(freqs)
        return [heapq.heappop(freqs)[1] for _ in range(k)]