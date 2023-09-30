/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 *
 * https://leetcode.com/problems/two-sum/description/
 *
 * algorithms
 * Easy (50.74%)
 * Likes:    51936
 * Dislikes: 1700
 * Total Accepted:    11M
 * Total Submissions: 21.6M
 * Testcase Example:  '[2,7,11,15]\n9'
 *
 * Given an array of integers nums and an integer target, return indices of the
 * two numbers such that they add up to target.
 * 
 * You may assume that each input would have exactly one solution, and you may
 * not use the same element twice.
 * 
 * You can return the answer in any order.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [2,7,11,15], target = 9
 * Output: [0,1]
 * Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [3,2,4], target = 6
 * Output: [1,2]
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: nums = [3,3], target = 6
 * Output: [0,1]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 2 <= nums.length <= 10^4
 * -10^9 <= nums[i] <= 10^9
 * -10^9 <= target <= 10^9
 * Only one valid answer exists.
 * 
 * 
 * 
 * Follow-up: Can you come up with an algorithm that is less than O(n^2) time
 * complexity?
 */

// @lc code=start
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using std::vector;
using std::cout;
using std::endl;

class Solution {
public:
    vector<int> twoSum(std::vector<int>& nums, int target) {
        vector<int> result;
        // map to store the index of each element
        std::unordered_map<int, int> indexMap;
        // iterate through the vector
        for (int i = 0; i < nums.size(); ++i) {
            // check if the map contains the complement
            if (indexMap.find(target - nums[i]) != indexMap.end()) {
                // if it does, add the current index and the index of the complement to the result vector
                result.push_back(indexMap[target - nums[i]]);
                result.push_back(i);
                break;
            }
            // if it doesn't, add the current element to the map
            indexMap[nums[i]] = i;
        }
        return result;
    }
};
// @lc code=end

