import random


def Binary_Search(a,n):
    left=0
    right=len(a)
    while left<right:
        mid=(left+right)//2
        if(a[mid]==n):
            print("Found")
            return
        elif n>a[mid]:
            left=mid+1

        else:
            right=mid-1

    print("Not Found")


a=[]
n=int(input("Enter the Size of the list"))
for i in range(n):
    a.append(random.randrange(1,100))

a.sort()
print(a)
elem=int(input("Enter the Searching element"))
Binary_Search(a,elem)
