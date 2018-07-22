import random




def Quick_Sort(a,l,r):
    if r>l:
        parti=partion(a,l,r)
        Quick_Sort(a,l,parti-1)
        Quick_Sort(a,parti+1,r)


def partion(a,l,r):
    pivot=a[r]
    i=l-1
    for j in range(l,r):
        if a[j]<=pivot:
            i=i+1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[r]=a[r],a[i+1]
    return i+1





a=[]
n=int(input("Enter the Size of the list"))
for i in range(n):
    a.append(random.randrange(1,100))
print(a)
Quick_Sort(a,0,n-1)
print(a)
