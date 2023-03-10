"""
3. Longest Substring Without Repeating Characters

Input:          s = "abcabcbb"
Output:         3
Explanation:    The answer is "abc", with the length of 3.

Input:          s = "bbbbb"
Output:         1
Explanation:    The answer is "b", with the length of 1.
Example 3:

Input:          s = "pwwkew"
Output:         3
Explanation:    The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

"""
Sliding window solution with iteration through string to find repeated char.
"""
# def lengthOfLongestSubstring(s: str) -> int:
#     max_len, lidx = 0, 0
#     for ridx in range(len(s)):
#         # finding longest ss starting at index i
#         new_lidx = s.find(s[ridx], lidx, ridx)
#         if new_lidx != -1:
#             lidx = new_lidx + 1
#         max_len = max(max_len, ridx - lidx + 1)
#     return max_len

"""
Sliding window solution with hashtable to find repeated char.
Theoretically faster but doesn't seem to make much difference,
at least on small strings.
"""
def lengthOfLongestSubstring(s: str) -> int:
    max_len, l_idx = 0, 0
    last_seen = dict()
    for r_idx in range(len(s)):
        # finding longest substring starting at index i
        l_idx = max(l_idx, last_seen.get(s[r_idx], -1) + 1)
        max_len = max(max_len, r_idx - l_idx + 1)
        last_seen[s[r_idx]] = r_idx
    return max_len

test_cases = {
    "abcabcbb": 3,
    "bbbbb": 1,
    "pwwkew": 3,
    "abcadcef": 5
}
for args, answer in test_cases.items():
    ret = lengthOfLongestSubstring(args)
    if ret == answer:
        print("Correct:", answer, "Input:", args, sep="\t")
    else:
        print("Incorrect:", ret, "Correct:", answer, "Input:", args, sep="\t")

