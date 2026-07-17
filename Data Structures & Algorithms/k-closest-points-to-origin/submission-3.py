class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        array_of_dis = []
        for p in points:
            array_of_dis.append((self.euclidean(p), p))
        
        heapq.heapify(array_of_dis)
        result = []
        for i in range(k - 1):
            result.append(heapq.heappop(array_of_dis)[1])
        dis = array_of_dis[0][0]
        result.append(heapq.heappop(array_of_dis)[1])
        while len(array_of_dis) > 0:
            if array_of_dis[0][0] != dis:
                break
            result.append(heapq.heappop(array_of_dis)[1])
        return result

    def euclidean(self, c1):
        return math.sqrt((c1[0] - 0)**2 + (c1[1] - 0)**2)