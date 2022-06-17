class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        degree = collections.Counter()

        for dest, orig in prerequisites:
            adj[orig].append(dest)
            degree[dest] += 1

        # Get origins
        bfs = [c for c in range(numCourses) if degree[c] == 0]

        for c in bfs:
            for n in adj[c]:
                degree[n] -= 1
                if degree[n] == 0:
                    bfs.append(n)

        return bfs if len(bfs) == numCourses else []
                    

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        degree = collections.Counter()
        
        for p in prerequisites:
            dest, org = p
            adj[org].append(dest)
            degree[dest] += 1
            if org not in degree:
                degree[org] = 0
        
        free = set(range(numCourses)) - set(degree)
        for f in free:
            degree[f] = 0
        
        for i in range(len(degree), numCourses):
            if i not in degree:
                degree[i] = 0
        
        stk = list(filter(lambda x: degree[x]==0, degree.keys()))
        
        rtn = []
        while stk:
            node = stk.pop()
            rtn.append(node)
            for nei in adj[node]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    stk.append(nei)
        
        return rtn * (len(rtn) == numCourses)
            