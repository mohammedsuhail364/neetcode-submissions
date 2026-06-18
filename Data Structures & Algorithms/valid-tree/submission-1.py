class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def dfs(i,parent):
            visit.add(i)
            for nei in adj[i]:
                if nei==parent:
                    continue
                if nei in visit:
                    return False 
                if not dfs(nei,i):
                    return False
            return True
        adj=defaultdict(list)
        visit=set()
        for src,dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        if not dfs(0,-1):
            return False
        return len(visit)==n