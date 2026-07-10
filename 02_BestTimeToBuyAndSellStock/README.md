[Back to Grind 75 List](../README.md)

# Best Time to Buy and Sell Stock

- LeetCode: [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)
- Difficulty: `Easy`
- Solution File: [main.py](./main.py)
- Status: `Implemented`

## Intuition

- We need to check the maximum profit by selling after buying.
- A brute-force nested loop works, but it checks too many pairs. 
- And it might be finding a day is the cheapest and looking for the best timing to sell, until we find a new timing to buy with a cheaper price.

### Answer: Optimal substructure, so that is Dynamic Programming

## Approach

1. Initialize `cost` as first day prices.
2. Iterate the prices start from second day.
3. If exists cheaper cost, then update cost
4. Else, check existence of larger profit, update profit if existed.

## Complexity

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`

## Other Resources

- [[演算法] 學習筆記— 15. Dynamic Programming 動態規劃](https://medium.com/@amber.fragments/%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98-dynamic-programming-%E5%8B%95%E6%85%8B%E8%A6%8F%E5%8A%83-9c83addce818)
- [從Dynamic Programming陣列到Kadane’s Algorithm](https://medium.com/@h42318/%E5%BE%9Edynamic-programming%E9%99%A3%E5%88%97%E5%88%B0kadanes-algorithm-8d7f75ddf02d)
