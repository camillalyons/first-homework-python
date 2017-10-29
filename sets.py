##Introduction to Sets
def average(array):
    numerator = (sum(set(array)))
    denominator = len(set(array))
    return (numerator/denominator)

##Symmetric Difference
M = input()
Mn = set(map(int,input().split()))
N = input()
Nn = set(map(int,input().split()))
out = list((Mn).symmetric_difference(Nn))
out.sort()
for el in out:
    print (el)

##No Idea!
n, m = list(map(int, input().split()))
array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
a = 0
for el in array:
    if el in A:
        a += 1
    if el in B:
        a -= 1
print (a)

##Set .add()
n = int(input())
s = set()
for i in range(n):
    line = str(input())
    s.add(line)
print (len(s))

##Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
N = int(input())
for el in range(N):
    c = input().split()
    if c[0] == 'pop':
        s.pop()
    if c[0] == 'remove':
        s.remove(int(c[1]))
    if c[0] == 'discard':
        s.discard(int(c[1]))
print (sum(s))

##Set .union() Operation
ne = int(input())
pe = set(map(int, input().split()))
nf = int(input())
pf = set(map(int, input().split()))
ef = pe.union(pf)
print (len(ef))

##Set .intersection() Operation
ne = int(input())
pe = set(map(int, input().split()))
nf = int(input())
pf = set(map(int, input().split()))
ef = pe.intersection(pf)
print (len(ef))

##Set .difference() Operation
ne = int(input())
pe = set(map(int, input().split()))
nf = int(input())
pf = set(map(int, input().split()))
ef = pe.difference(pf)
print (len(ef))

##Set .symmetric_difference() Operation
ne = int(input())
pe = set(map(int, input().split()))
nf = int(input())
pf = set(map(int, input().split()))
ef = pe.symmetric_difference(pf)
print (len(ef))

##Set Mutations
la = int(input())
A = set(map(int, input().split()))
nc = int(input())

for el in range(nc):
    cmd = input().split()[0]
    B = set(map(int, input().split()))
    eval('A.' + cmd +'(B)')
print (sum(A))

##The Captain's Room
k = int(input())
r = list(map(int, input().split()))    #the list of room numbers
rs = set(r)    #the set of r
srs = sum(rs)    #the sum of the set of r
sr = sum(r)    #the sum of all the room numbers
ksrs = (srs)*k    #multiplicating each room number in the set for its occurrance in the list
diff = ksrs-sr    #this difference is a multiple of the captain's room
cr = diff/(k-1)    #captain's room
print (int(cr))

##Check Subset
for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted.
    a = int(input()); A = set(input().split())
    b = int(input()); B = set(input().split())
    print (A.issubset(B))

##Check Strict Superset
A = set(map(int, input().split()))
nu = int(input())
res = []

for n in range(nu):  # getting all the N sets in a unique list
    c = set(map(int, input().split()))
    res.append(c)

result = True
for s in res:
    if not A >= s:
        result = False
print(result)