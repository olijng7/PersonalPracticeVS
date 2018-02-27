bigguy = max([2,3,4,5])
print(bigguy)

n = [[101,2],[12,3],[15,6],[101,10]]

def convert(x):
    q = str(x[0])
    ans = 0
    for i in range(0,len(q),1):
        ans += int(q[i]) * (x[1]**(len(q)-i-1))
    return ans

for i in n:
    print(convert(i)," ", end="")

x = list(range(1,11,2))
y = list(range(1,11,2))
print(x,y)

y = "abba"

def palin(x):
    revx = ''
    for i in range(len(x)-1,-1,-1):
        revx += x[i]
    if revx == x:
        return True
    else:
        return False

print(palin(y))

def tot_time(iv):
    t = iv/9.8
    return 2*t

print(tot_time(860))

def jl(x):
    y = 2*x
    return x+1
def g(x,y):
    def jl(x):
        if y > x:
            x = 3
            return x+1
        else:
            return y-x
    return jl(x+y)

x = 2
y = 3
print(x,y)
x = jl(x-y)+g(jl(y),2)
y = jl(y)
print(x,y)

dict = {1:2,4:5,11:17}
print(list(dict.keys()))

HexDict = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
def d(n,b):
    count = 0
    ans = ''
    j = True
    while j:
        if n//(b**count) >= b:
            count += 1
        else:
            j = False
    ntemp = n
    while count > -1:
        if ntemp//(b**count) >= 10:
            ans += HexDict[ntemp//(b**count)]
        else:
            ans += str(ntemp//(b**count))
        print(ans)
        ntemp = ntemp - (ntemp//(b**count)) * (b**count)
        print(ntemp)
        count -= 1
    return ans

print(d(200,16))
print('\n')
print(d(689,16))