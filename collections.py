##collections.Counter()
x = int(input())
ss = list(map(int, input().split()))
n = int(input())
tot = 0
for line in range(n):
    c = list(map(int, input().split()))
    if c[0] in list(ss):
        tot += c[1]
        ss.remove(c[0])
print (tot)

##DefaultDict Tutorial
from collections import defaultdict

d = defaultdict(list)
l = []
n, m = map(int, input().split())

# creating a default dictionary with the words of group A and their indices
for i in range(n):
    d[input()].append(i + 1)

for i in range(m):
    l.append(input())

for w in l:
    if w in d:
        print(' '.join(map(str, d[w])))
    else:
        print(-1)

##Collections.namedtuple()
n,m = int(input()), input().split().index('MARKS')    #m indicates the position of 'MARKS' among the 4 coloums
ma = []
for line in range(n):
    ma.append(float(input().split()[m]))
print (sum(ma)/n)

##Collections.OrderedDict()
from collections import OrderedDict
n = int(input())
l = OrderedDict()
items = []
#creating an ordered dictionary with the products as keys and their prices as values
for i in range(n):
    c = input().split()
    price = int(c[-1])
    item = ' '.join(c[:-1])
    items.append(item)
    l[item]=price

for key in l:
    co = int(items.count(key))    #the occurrance of each product
    print (key, int(l[key])*co )

##Word Order
from collections import Counter
n = int(input())
w = []
for i in range(n):
    c = (input().strip())
    w.append(c)
c = Counter(w)
print (len(c))

for word in w:
    p = c.pop(word, None)    #if word isn't in c, it will return 'None'
    if p != None:
        print (p, end = ' ')

##Collections.deque()
from collections import deque
d = deque()

n = int(input())
for i in range(n):
    c = input().split()
    com = c[0]
    arg = c[-1]
    if len(c) == 1:
        eval('d.' + com + '()')
    else:
        eval('d.' + com + '(' + arg + ')')
for el in d:
    print (el, end = ' ')

##Piling Up!
from collections import deque
t = int(input())
for i in range(t):
    n = int(input())
    c = deque(map(int, input().strip().split()))
    m = 0
    f = []
    #creating a sorted list with all the numbers given
    while m < n:
        if c[0] >= c[-1]:
            f.append(c[0])
            c.popleft()
        else:
            f.append(c[-1])
            c.pop()
        m += 1

    if f == sorted(f)[::-1]:    #if f is in decreasing order
        print ('Yes')
    else:
        print ('No')

##Most Common
import sys

if __name__ == "__main__":
    s = input().strip()

from collections import Counter
c = sorted(Counter(s).items(), key = lambda x: (-x[1],x[0]))
for w, co in c[:3]:
    print (w, co)