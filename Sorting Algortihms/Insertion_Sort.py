import random

def Insertion_Sort(a):
    length=len(a)
    for i in range(length):
        j=i-1
        temp=a[i]
        while j>=0 and temp<a[j]:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=temp


a=[]
n=int(input("Enter the Size of the list"))
for i in range(n):
    a.append(random.randrange(1,100))
print(a)
Insertion_Sort(a)
print(a)
