class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def dfs(node,parent,visit):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei,node,visit):
                    return False
            return True
            
        adj=defaultdict(list)
        visit=set()
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

            
        if not dfs(0,-1,visit):
            return False

        return len(visit)==n