##Lists
if __name__ == '__main__':
    N = int(input())
out = ''
lst = list()
for line in range(N):
    i = input().split()
    comand = i[0]    #the word
    arguments = i[1:]    #the (eventual) numbers
    if comand == 'print':
        print (lst)
    else:
        c = out + '.' + comand + '('+ ','.join(arguments) +')'
        eval('lst'+c)

##Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
t = tuple(integer_list)
print (hash(t))

##List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
print ([[i,j,k] for i in  range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n])

##Find the Second Largest Number
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
arr.sort()
while arr[-1] == arr[-2]:
    arr.pop()
print (arr[-2])

##Nested Lists
if __name__ == '__main__':
    array = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        array += [[name, score]]    #created a list of lists with name, score

#getting the second lowest score
ss = []
for n,s in array:
    ss.append(s)
sls = sorted(set(ss))[1]

#getting all the students with second lowest score and printing them in alphabetical order
f = []
for n,s in array:
    if s == sls:
        f.append(n)
for na in sorted(f):
    print (na)

##Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

theScores = student_marks[query_name]
average = sum(theScores)/3
print ("{0:.2f}".format(average))