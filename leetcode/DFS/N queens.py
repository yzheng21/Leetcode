'''
n皇后问题是将n个皇后放置在n*n的棋盘上，皇后彼此之间不能相互攻击。

给定一个整数n，返回所有不同的n皇后问题的解决方案。

每个解决方案包含一个明确的n皇后放置布局，其中“Q”和“.”分别表示一个女王和一个空位置。
'''

class solution:

    def solveNqueen(self,n):

        def attack(row,col):
            for i in range(row):
                if abs(cols[i] - col) == abs(i - row) or cols[i] == col:
                    return False
            return True

        def search(row,result):
            if row == n:
                results.append(result)
                return

            for col in range(n):
                if attack(row,col):
                    cols[row] = col
                    s = '.' * n
                    search(row + 1,result + [s[:col]+'Q'+s[col+1:]])

        cols = [-1] * n
        results = []
        search(0,[])
        return results

res = solution().solveNqueen(4)
print(res)
