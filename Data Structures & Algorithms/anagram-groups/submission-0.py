class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s) #Here the array is the key in that case: "80,81,82" in ASCII for example and the values is the actual word. That way if there are other words with the same key structure they will get appended to the same value list
        return list(res.values()) #We just get the values since they are just multiple lists within a larger list but in hashmap format

        # The key learning point here is to understand how you can use HashMaps efficiently to manipulate the data.
