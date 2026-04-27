class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node,parent):
            if node in visit:
                return
            visit.add(node)
            for nei in adj[node]:
                if nei!=parent:
                    dfs(nei,node)
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit=set()
        component=0
        for i in range(n):
            if i not in visit:
                dfs(i,-1)
                component+=1
        return component
