[Back to Grind 75 List](../README.md)

# 3Sum

- LeetCode: [3Sum](https://leetcode.com/problems/3sum)
- Difficulty: `Medium`
- Solution File: [main.py](./main.py)
- Status: `Implemented`

## Intuition

- Take a number as target which is `a = nums[i]`, them problems will become Two Sum Problem with target `b + c = -a`.
- Answer only require unique triplets, and order of triplets do not matter. No need indexing information.
- First, we can sort the arrays such that duplicated target `a` can be easily ignored by comparing `nums[i] == nums[i - 1]`.
- Since, we had already sort the arrays, we can solve Two Sum Problem by Two Pointer `left < right` in one loop.

### Answer: Sorting & Two Pointer

## Approach

1. Sort the arrays
2. Take a number as first of the triplet. `target = -nums[i]`. Also we will ignore duplicated numbers.
3. Use two pointers on the remaining numbers. `sum = num[l] + num[r] = -target`
4. Move pointers on sorted subarray. 
    - `l++` = larger `sum`.
    - `r--` = smaller `sum`.
5. Skip duplicated numbers
    - `nums[l] == nums[l - 1]` since `l++`
    - `nums[r] == nums[r + 1]` since `r--`

## Complexity

- Time Complexity: `O(n^2)`
    - Sorting: `O(nlogn)`
    - Nested Loop: `O(n^2)`
- Space Complexity: `O(1)`
    - Just using pointers and results array

## Notes

- Using one pass hash map to solve Two Sum Problem is also available. But using more spaces and wasting sorted advantages.

## Other Resources