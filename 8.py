L1 = [1,2,3,4,5]
L2 = []
for i in L1:
    L2.insert(0,i)
    print(L2)


n = int(input())
while n > 0:
    print(n % 10)
    n = n // 10