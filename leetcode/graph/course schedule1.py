class solution(object):
    def course(self,numcourse,prerequisties):
        queue = []
        finished_course = []
        pre_graph = {x: set() for x in range(numcourse)}
        for c, p in prerequisties:
            pre_graph[c].add(p)

        #add nodes with no pre
        for c in pre_graph:
            if not pre_graph[c]:
                queue.append(c)
        # For each of the remaining node, remove its prerequisites in queue;
        # if node has no prerequisites, add it to queue, and repeat
        while queue:
            u = queue.pop(0)
            for v, pres in pre_graph.items():
                if u in pres:
                    pres.remove(u)
                    if not pres:
                        queue.append(v)
            finished_course.append(u)
        return len(finished_course) == numcourse
