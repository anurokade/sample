def add(b):
    sum=0
    for i in b:
       sum+=i
    print(sum)



T=int(input())
for i in range (T):
    a=[int(x) for x in input().split()]
    add(a)
