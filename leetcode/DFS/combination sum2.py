class solution:
    def combinationsum2(self,candidates,target):
        candidates.sort()
        self.res, used = [], [0]*len(candidates)
        self.dfs(candidates,target,0,[],used)
        return self.res

    def dfs(self,candidates,target,start,tmp,used):
        if target == 0:
            return self.res.append(tmp)
        for i in range(start,len(candidates)):
            if candidates[i] > target or (i > 0 and candidates[i] == candidates[i-1] and used[i-1] == 0):
                continue
            #tmp.append(candidates[i])
            used[i] =1
            self.dfs(candidates,target-candidates[i],i+1,tmp+[candidates[i]],used)
            #tmp.pop()
            used[i] = 0

res = solution().combinationsum2([10,1,2,7,6,1,5],8)
print(res)

