'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Input: s = "A", numRows = 1
Output: "A"


Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''


def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    k = 2 * (numRows - 1)
    ret = ""
    for i in range(numRows):
        for j in range(0, len(s) + k, k):
            if i != 0 and i != numRows - 1 and 0 <= j-i < len(s):
                ret += s[j-i]
            if j + i < len(s):
                ret += s[j+i]
    return ret


test_cases = {
    ("PAYPALISHIRING", 3): "PAHNAPLSIIGYIR",
    ("PAYPALISHIRING", 4): "PINALSIGYAHRPI",
    ("A", 1): "A",
    ("A", 2): "A",
    ("ABCD", 3): "ABDC"
}

for args, answer in test_cases.items():
    ret = convert(*args)
    if ret == answer:
        print("Correct:", answer, "Input:", args, sep="\t")
    else:
        print("Incorrect:", ret, "Correct:", answer, "Input:", args, sep="\t")
