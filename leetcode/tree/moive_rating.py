'''
给一些movie（编号从0开始）的rating和他们的联系关系，联系关系可以传递(a和b有联系，b和c有联系，a和c也认为有联系)。给出每个movie的直接联系list。再给定一个movie编号为S，找到和S相联系的movie中的rating最高的K个movie（当与S相联系的movie少于K个时，输出所有。输出答案时可以按照任意次序，注意联系movie并不包括S。）
'''

import queue
class Solution:
    """
    @param rating: the rating of the movies
    @param G: the realtionship of movies
    @param S: the begin movie
    @param K: top K rating
    @return: the top k largest rating moive which contact with S
    """
    def __init__(self):
        self.visit = {}
        self.q = queue.PriorityQueue()
    class node:
        def __init__(self,rating,id):
            self.id = id
            self.rating = rating
        def __cmp__(self, other):
            return self.rating > other.rating

    def dfs(self, u , limit, rating, G, S):
        self.visit[u] = 1
        first = self.node(0,0)
        if self.q.qsize() != 0:
            first = self.q.get()
            self.q.put(first)
        if u != S:
            if self.q.qsize() < limit or rating[u] > first.rating:
                if self.q.qsize() == limit:
                    self.q.get()
                self.q.put(self.node(rating[u],u))
        for i in G[u]:
            if i not in self.visit:
                self.dfs(i,limit,rating,G,S)

    def topKmoive(self,rating,G,S,K):
        ans = []
        self.dfs(S,K,rating,G,S)
        while self.q.empty() is False:
            ans.append(self.q.get().id)
        return ans