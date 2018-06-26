# BFS
#O(n*L), n is length of string, L is size of directionary

class solution(object):
    def ladderlength(self,beginword,endword,wordlist):
        distance,cur,visited,lookup = 0, [beginword], set([beginword]),set(wordlist)
        while cur:
            next_queue = []
            for word in cur:
                if word == endword:
                    return distance + 1
                for i in range(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i+1:]
                        if candidate not in visited and candidate in lookup:
                            next_queue.append(candidate)
                            visited.add(candidate)
            distance += 1
            cur = next_queue
        return 0

if __name__ == '__main__':
    print(solution().ladderlength('hit','cog',set(['hot','dot','dog','lot','log','cog'])))

