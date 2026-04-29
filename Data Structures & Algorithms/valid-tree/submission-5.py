class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent=list(range(n+1))
        rank=[1]*(n+1)
        self.comps=n
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]] # path compression
                x=parent[x]
            return x

        def union(x,y):
            px,py = find(x),find(y)
            if px==py:
                return False # cycle detected
            if rank[px]<rank[py]:
                px,py=py,px
            self.comps-=1
            parent[py]=px
            rank[px]+=rank[py]
            return True

        for u,v in edges:
            if not union(u,v):
                return False # cycle detected
        return self.comps==1