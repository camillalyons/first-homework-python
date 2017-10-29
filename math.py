##Polar Coordinates
import cmath
polar = cmath.polar(complex(input()))
print(polar[0])
print(polar[1])

##Find Angle MBC
import math
ab=int(input())
bc=int(input())
A = math.atan2(ab,bc)    #calculating the angle in radiants
ADeg = math.degrees(A)      #converting the angle in degrees
ADeg = int(round(ADeg))
print (str(ADeg)+'°')

##Triangle Quest 2
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print ((10**i//9)**2)

##Mod Divmod
a = int(input())
b = int(input())
print (a//b)
print (a%b)
print (divmod(a,b))

##Power - Mod Power
a = int(input())
b = int(input())
m = int(input())
print (pow(a,b))
print (pow(a,b,m))

##Integers Come In All Sizes
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print (a**b+c**d)

##Triangle Quest
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print (i*(10**i//9))