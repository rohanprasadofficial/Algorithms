import random

def Bubble_Sort(a):
    n=len(a)
    for i in range(n):
        flag=0
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j+1],a[j]=a[j],a[j+1]
                flag=1
        if flag==0:
            break

a=[]
n=int(input("Enter the Size of the list"))
for i in range(n):
    a.append(random.randrange(1,100))

print(a)
Bubble_Sort(a)
print(a)
