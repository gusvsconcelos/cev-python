# class Solution:
#    def __init__(self, s):
#        self.s = s
#
#    def result(self):
#        unique_chars = set(self.s)
#
#        min_index = len(self.s)
#
#        for char in unique_chars:
#            if self.s.count(char) == 1:
#                min_index = min(min_index, self.s.index(char))
#
#        if min_index < len(self.s):
#            print(min_index)
#        else:
#            print(-1)
#
#
# solution = Solution('leetcode')
#
# solution.result()

s = "loveleetcode"

unique_chars = set(s)

min_index = len(s)

for char in unique_chars:
    if s.count(char) == 1:
        min_index = min(min_index, s.index(char))

if min_index < len(s):
    print(min_index)
else:
    print(-1)
