class solution(object):
    def numofislands(self,grid):
        directions = {'l':[-1,0],'r':[1,0],
                      'u':[0,1],'d':[0,-1]}
        def dfs(i,j,grid,island):
            if not(0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] > 0):
                return False
            grid[i][j] += -1   #遍历过的全部-1
            for k, v in directions.items():
                island.append(k)
                dfs(i+v[0],j+v[1],grid,island)
            return True

        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                island = []
                if dfs(i,j,grid,island):
                    islands.add(''.join(island))
        return len(islands)
