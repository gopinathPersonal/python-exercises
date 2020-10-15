import math
class Solution:
    def minTimeToVisitAllPoints(self, points):
        rows = len(points)
        minTime = 0

        for i in  range(0, rows-1):
            xdiff = abs(points[i][0] - points[i+1][0])
            ydiff = abs(points[i][1] - points[i+1][1])
            print(max(xdiff, ydiff))
            minTime = minTime + max(xdiff, ydiff)
        return minTime


a = Solution()
result = a.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])
print(result)