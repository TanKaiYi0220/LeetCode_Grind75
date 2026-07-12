[Back to Grind 75 List](../README.md)

# Product of Array Except Self

- LeetCode: [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self)
- Difficulty: `Medium`
- Solution File: [main.py](./main.py)
- Status: `Implemented`

## Intuition

- Product of array except self without using division operation.
- By observation, we can found that answer for any `nums[i]` is product of `nums[0], ..., nums[i - 1]` and `nums[i + 1], ..., nums[length]`, which is product of prefix array and suffix array.

### Answer: Product of Prefix Array and Suffix Array

## Approach

1. A loop to calculate the product of prefix array
    - Create variable `prefix`
    - Store `prefix` into `out[i]` before multiply itself `prefix *= nums[i]`
2. A loop to calculate the product of suffix array
    - Create variable `suffix`
    - Multiply `suffix` into `out[i]` before multiply itself `suffix *= nums[i]`

## Complexity

- Time Complexity: `O(n)`
    - Two simple loops
- Space Complexity: `O(1)`
    - Only using output array and two variable (can be used as one)

## Other Resources