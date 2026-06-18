class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # this is similiar to course schedule II only difference is to make the adj list 
        # this is the case ["hrn","hrf","er","enn","rfnn"]
        # e->h this means h comes befor e
        # r->e e comes before r 
        # n->f n comes before f
        # after find the adj list we can run a khans algorithm we get res
        adj=defaultdict(set)
        indegree={c:0 for word in words for c in word}
        # same set up like course schedule II
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            min_len=min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:min_len]==w2[:min_len]:
                return "" # impossible case imagine like this ["abc","ab"] no dictionary looks like this 
            for j in range(min_len):
                for j in range(min_len):
                    if w1[j]!=w2[j]: # find the different char
                        if w2[j] not in adj[w1[j]]:
                            adj[w1[j]].add(w2[j]) # which comes first is the key
                            indegree[w2[j]]+=1 
                        break
        q=deque([k for k,v in indegree.items() if v==0])
        # kahn's algorithm (topological sort)
        res=""
        while q:
            node=q.popleft()
            res+=node
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        if len(res) < len(indegree):
            return ""    # cycle detected
        return "".join(res)