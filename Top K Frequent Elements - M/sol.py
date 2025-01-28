class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)
        for i in range(len(nums)):
            hmap[nums[i]] += 1
        res = []
        for i in range(k):
            key_with_max_value = max(hmap, key=hmap.get)
            res.append(key_with_max_value)
            del hmap[key_with_max_value]
        return res
