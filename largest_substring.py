#Longest Substring Without Repeating Characters
'''
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''

def lengthOfLongestSubstring(mystring):
    n = len(mystring)
    longest = 0
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if mystring[j] in seen: break
            seen.add(mystring[j])
        longest = max(len(seen), longest)
    return longest

mystring = input("enter the string: ")
print(lengthOfLongestSubstring(mystring))

