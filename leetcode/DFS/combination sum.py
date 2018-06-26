class solution:
    def combinationsum(self,candidates, target):
        candidates = list(set(candidates))
        candidates.sort()
        self.res = []
        self.DFS(candidates,target,0,[])
        return self.res

    def DFS(self,candidates,target,start,valuelist):
        length = len(candidates)
        if target == 0:
            return self.res.append(valuelist)
        for i in range(start,length):
            if target < candidates[i]:
                return
            self.DFS(candidates,target-candidates[i],i,valuelist + [candidates[i]])

res = solution().combinationsum([2,3,6,7],7)
print(res)
