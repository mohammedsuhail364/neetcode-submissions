from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def bfs(i):
            q=deque([(i)])
            visit.add(i)
            while q:
                node=q.popleft()
                for nei in adj[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
             
        adj=defaultdict(list)
        for src,dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        res=0
        visit=set()
        for i in range(n):
            if i not in visit:
                bfs(i)
                res+=1
        return res
        