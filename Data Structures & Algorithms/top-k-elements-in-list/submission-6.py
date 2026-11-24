class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kmost = defaultdict(list)
        numdict = defaultdict(list)
        # numsset = set(nums)

        # for num in numsset:
        #     currentCount = nums.count(num)
        #     kmost[currentCount].append(num)

        for num in nums:
            if num not in numdict:
                numdict[num] = 0
            numdict[num] += 1

        for num in numdict:
            count = numdict[num]
            kmost[count].append(num)
        
        counts = list(kmost.keys())
        counts.sort(key=int, reverse=True)
        output = []
        counter = 0
        for count in counts:
            output.extend(kmost.get(count))
            counter+=len(kmost.get(count))
            if counter == k:
                break
        return output
        
