from typing import List

def findCircleNum(self, isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    visited = [False] * n

    def dfs(city):
        for j in range(n):
            if isConnected[city][j] == 1 and not visited[j]:
                visited[j] = True
                dfs(j)

    provinces = 0
    for i in range(n):
        if not visited[i]:
            provinces += 1
            visited[i] = True
            dfs(i)
    
    return provinces

