from itertools import combinations
n = input()

s = list(input().split(' '))

k = int(input())

c = 0

for i in combinations(s,k):
    if 'a' in i:
        c=c+1
print(c/len(list(combinations(s,k))))