strs = ["aaa","aa","aaa"]
from typing import List
s =""

if len(strs) == 0 :
    s=""
    print(s)
if len(strs) == 1 :
    print(strs[0])

strs.sort()
valmin = min(len(strs[0]), len(strs[len(strs)-1]))
print(valmin)
i=0
while i< valmin and strs[0][i] ==strs[len(strs)-1][i]:
    i +=1
print(strs[0][0:i])

x = [0,1,1,1,11]
print(x[-1])

