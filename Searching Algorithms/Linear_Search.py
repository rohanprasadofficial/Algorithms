import random


def linear_search(a, n):
    for i in a:
        if i==n:
            print("Found")
            return
    print("Not Found")


a=[]
n=int(input("Enter the Size of the list"))
for i in range(n):
    a.append(random.randrange(1,100))

#print(a)
elem=int(input("Enter the Searching element"))
linear_search(a,elem)
