s = "abbaca"
print(s)
map = {}
for i in range(0, len(s)):
    if s[i] in map:
        map[s[i]]+=1
    else:
        map[s[i]]=1
print(map) 

for key,value in map.items():
    if value > 1:
        print(key)
           