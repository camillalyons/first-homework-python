##Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")

##Python If-Else
if __name__ == '__main__':
    n = int(input())
if 6<=n<=20 or n%2==1:
    print ('Weird')
else:
    print ('Not Weird')

##Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
print (a+b)
print (a-b)
print (a*b)

##Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
print (a//b)
print (a/b)

##Loops
if __name__ == '__main__':
    n = int(input())
for num in range(n):
    print (num**2)

##Write a function
def is_leap(year):
    leap = False
    if year%4 == 0:
        leap = True
        if year%100 == 0:
            leap = False
        if year% 400 == 0:
                leap = True
    return (leap)


##Print Functionif __name__ == '__main__':
    n = int(input())
for el in range(1,n+1):
    print (el, end='')