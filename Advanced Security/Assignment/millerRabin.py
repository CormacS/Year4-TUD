#Used a guide to help explain algorithim

import random
 
def trial_composite(a):
    if pow(a, d, num) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, num) == num-1:
            return False
    return True  

num = 6
if num!=int(num):
    x =  False
num=int(num)
s = 0
d = num-1
while d%2==0:
    d>>=1
    s+=1
assert(2**s * d == num-1)

for i in range(8):
    a = random.randrange(2, num)
    if trial_composite(a):
        x= False
    else:
        x = True

if x == True:
    print("Composite")
else:
    print("Inconclusive")