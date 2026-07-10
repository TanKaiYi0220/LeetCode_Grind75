[Back to Grind 75 List](../README.md)

# Two Sum

- LeetCode: [Two Sum](https://leetcode.com/problems/two-sum)
- Difficulty: `Easy`
- Solution File: [main.py](./main.py)
- Status: `Implemented`

## Intuition

- We need to find two values whose sum equals the target.
- A brute-force nested loop works, but it checks too many pairs.
- A hash map lets us remember numbers we have already seen and check the needed complement quickly.

## Approach: One-Pass Hash Map

1. Create a hash map (`num_map`) that stores each number and its index.
2. Loop through the array once with `enumerate(nums)`.
3. For each number `n`, compute the complement `dn = target - n`.
4. If `dn` is already in the hash map, return the saved index and the current index.
5. Otherwise, store the current number and index in the hash map and continue.

## Complexity

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

## Other Resources

- [Python Data Structures: Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Python Time Complexity Reference](https://wiki.python.org/moin/TimeComplexity)
