# Time:  O(n)
# Space: O(n)

import collections


# DFS solution.
class solution(object):
    def killprocess(self,pid,ppid,kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        def killall(pid,children,killed):
            killed.append(pid)
            for child in children[pid]:
                killall(child,children,killed)

        result = []
        children = collections.defaultdict(set)

        for i in range(len(pid)):
            children[ppid[i]].add(pid[i])
        killall(kill,children,result)
        return result
