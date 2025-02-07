N=int(input("N ni kiriting : "))
sum=0
while N>=0:
    print(N)
    sum+=N%10
    N=N//10
print(sum)



