class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        li=defaultdict(list)
        for i in strs:
            count=[0]*26
            for x in i:
                count[(ord(x)-ord('a'))]+=1
            li[tuple(count)].append(i)
        return li.values()