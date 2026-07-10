class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # [[1, 3], [6, 9]]
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # [0, 1, 0, 1, 0, 0, 1, 1, 1, 1]

        # [2, 5]
        # 2 > 1, 2 < 3
            # 5 > 1, 5 > 3
            # 5 < 6 - STOP [R] but last iter did not stop 5 > 3 (max(5, 3))
        # [1, 5]

        # [[1,2],[3,5],[6,7],[8,10],[12,16]]
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16]
        # [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]

        # [4, 8]
        # 4 > 3, 4 < 5
            # 8 > 3, 8 > 5
            # 8 > 6, 8 > 7
            # 8 = 8, 8 < 10 - STOP [R]
            # 8 < 12 - STOP [R] but also stop at last iter 8 < 10 (max(8, 10))
        # [3, 10]

        n = len(intervals)
        out = []

        i = 0
        L = newInterval[0]
        R = newInterval[1]

        while i < n:
            # L -- [i][1] -- [i+1][0]
            if intervals[i][1] >= L: # there must be a number start from this interval
                break
            i += 1

        out.extend(intervals[:i])

        while i < n:
            # R -- [i][0]
            if intervals[i][0] > R:
                break

            # L -- [i][0] -- [i][1] -- [i+1][0]
            # [i][0] -- L -- [i][1] -- [i+1][0]
            L = min(L, intervals[i][0])

            # R -- [i-1][1] -- [i][0]
            # [i-1][1] -- R -- [i][0]
            R = max(R, intervals[i][1])
            i += 1

        out.append([L, R])
        out.extend(intervals[i:])

        return out

