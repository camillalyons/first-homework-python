##sWAP cASE
def swap_case(s):
    outPut = ""
    for letter in s:
        if letter.islower():
            outPut += letter.upper()
        else:
            outPut += letter.lower()
    return outPut

##String Split and Join
def split_and_join(line):
    return line.replace(" ", "-")

##What's Your Name?
def print_full_name(a, b):
    print ("Hello {} {}! You just delved into python.".format(a,b))

##Mutations
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

##Find a string
def count_substring(string, sub_string):
    ls = len(string)
    lss = len(sub_string)
    outPut = 0
    for pos in range(0, ls):
        temp = string[pos:pos + lss]
        if temp == sub_string:
            outPut += 1
    return outPut

##String Validators
if __name__ == '__main__':
    s = input()
    sIsalnum = False
    sIsalpha = False
    sIsdigit = False
    sIslower = False
    sIsupper = False
    for el in s:
        if (el.isalnum()):
            sIsalnum = True
        if (el.isalpha()):
            sIsalpha = True
        if (el.isdigit()):
            sIsdigit = True
        if (el.islower()):
            sIslower = True
        if (el.isupper()):
            sIsupper = True
    print (sIsalnum)
    print (sIsalpha)
    print (sIsdigit)
    print (sIslower)
    print (sIsupper)

##Text Alignment
#Replace all ______ with rjust, ljust or center.

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

##Text Wrap
def wrap(string, max_width):
    return textwrap.fill(string, max_width)

##Designer Door Mat
N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in range(1,N,2):
    print (('.|.'*i).center(M,'-'))
print ('WELCOME'.center(M, '-'))
for i in range(N-2,-1,-2):
    print (('.|.'*i).center(M,'-'))

##String Formatting
def print_formatted(number):
    w = len(bin(number)[2:])
    for n in range(number+1)[1:]:
        oc = oct(n)[2:]
        he = str(hex(n)[2:]).upper()
        bi = bin(n)[2:]
        print ('{:>{width}} {:>{width}} {:>{width}} {:>{width}}'.format(n, oc, he, bi, width=w))

##Alphabet Rangoli
def print_rangoli(size):
    import string
    s = string.ascii_lowercase

    s = s[:size][::-1]  # getting only the letters I need
    # creating a list with numbers going from 1 to n to 1
    r = list(range(size + 1)) * 2
    r1 = r[:size + 1]  # first half of r
    r2 = r[size + 1:]  # second half of n
    r1 = r1[1:-1]  # eliminating the 0 and the last numbers
    r2 = r2[1:][::-1]  # eliminating the 0 and reversing
    r = r1 + r2

    for line in r:
        hl = '-'.join(s[:line]).rjust(2 * size - 1, '-')  # creating only the first half of each line
        ht = hl + hl[::-1][1:]
        print(ht)

##Capitalize!
def capitalize(string):
    out = []
    space = ' '
    for word in string.split(' '):
        out.append(word.capitalize())
    return space.join(out)

##The Minion Game
def minion_game(string):
    vowels = 'AEIOU'
    kevinPoints = 0
    stuartPoints = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevinPoints += (len(string) - i)
        else:
            stuartPoints += (len(string) - i)

    if kevinPoints > stuartPoints:
        print('Kevin', kevinPoints)
    elif kevinPoints < stuartPoints:
        print('Stuart', stuartPoints)
    else:
        print('Draw')

##Merge the Tools!
def merge_the_tools(string, k):
    for sub in zip(*[iter(string)] * k):
        jsub = ''.join(sub)
        out = []
        for el in jsub:
            if el not in out:
                out.append(el)
        print (''.join(out))