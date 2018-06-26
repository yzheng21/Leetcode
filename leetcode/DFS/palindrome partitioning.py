class solution:
    def ispalindrome(self,s):
        for i in range(len(s)):
            if s[i] != s[len(s)-1-i]:
                return False
        return True

    def main(self,s):
        self.res = []
        self.dfs(s,[])
        return self.res

    def dfs(self,s,stringlist):
        if len(s) == 0:
            return self.res.append(stringlist)
        for i in range(1,len(s)+1):
            if self.ispalindrome(s[:i]):
                self.dfs(s[i:],stringlist+[s[:i]])

res = solution().main('aab')
print(res)