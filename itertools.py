##itertools.product()
import itertools
A = map(int, input().split())
B = map(int, input().split())
for i in itertools.product(A,B):
    print(i, end=' ')

##itertools.permutations()
from itertools import permutations
i, k = input().split()
for el in permutations(sorted(i), int(k)):
    print (''.join(el))

##itertools.combinations()
from itertools import combinations
s, k = input().split()
for i in range(1, int(k)+1):
    for j in combinations(sorted(s), i):
        print (''.join(j))

##itertools.combinations_with_replacement()
from itertools import combinations_with_replacement
s, k = input().split()
for j in combinations_with_replacement(sorted(s), int(k)):
    print (''.join(j))

##Compress the String!
from itertools import groupby
x = input()
s = groupby(x, int)
for k,g in s:
    G = len(list(g))
    print ((G, k), end=' ')

##Iterables and Iterators
from itertools import combinations
from decimal import Decimal
ll = int(input())
l = str(input()).split()
k = int(input())
c = 0
comb = (list(combinations(l,k)))
for li in comb:
    if 'a' in li:
        c += 1
n = Decimal(c/float(len(comb)))
print (round(n,3))

##Maximize It!
from itertools import product
k, m = map(int,input().split())
cc = []
for i in range(k):
    c = list(map(int, input().split()))
    n = c.pop(0)
    cc.append(c)
comb = list(product(*cc))

print (max([sum(map(lambda x: x**2, lst))%m for lst in comb]))