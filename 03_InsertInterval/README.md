[Back to Grind 75 List](../README.md)

# Insert Interval

- LeetCode: [Insert Interval](https://leetcode.com/problems/insert-interval)
- Difficulty: `Medium`
- Solution File: [main.py](./main.py)
- Status: `Implemented`

## Intuition

- Find the interval that start to insert and end to exit.
- Using lower bounds of new interval to find out where to enter. Using upper bounds of new interval to find out where to exit. Middle waypoint (intervals) should be merged.

## Approach

1. Iterate all of intervals, find interval to enter by `intervals[i][1] >= L` which means that there must be a number start from this intervals
2. Iterate remains of intervals, find interval to exit by `intervals[i][0] > R` which means that upper bounds did not reach this intervals. During this iteration, we record the new interval by comparing `L = min(L, intervals[i][0])` and `R = max(R, intervals[i][1])`
3. Extend output lists by remains of intervals

## Complexity

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

## Notes

- Why need to min/max condition? 
    - min
        - `# L -- [i][0] -- [i][1] -- [i+1][0]`
        - `# [i][0] -- L -- [i][1] -- [i+1][0]`
    - max
        - `# R -- [i-1][1] -- [i][0]`
        - `# [i-1][1] -- R -- [i][0]`

## Other Resources
