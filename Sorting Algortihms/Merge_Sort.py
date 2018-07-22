import random
def Merge_Sort(a):
    if len(a)>1:
        mid=len(a)//2
        leftpart=a[:mid]
        rightpart=a[mid:]
        Merge_Sort(leftpart)
        Merge_Sort(rightpart)
        c=[]

        j=0
        k=0
        i=0
        while i<len(leftpart) and j<len(rightpart):
            if(leftpart[i]>rightpart[j]):
                a[k]=rightpart[j]
                j=j+1
            else:
                a[k]=leftpart[i]
                i=i+1
            k=k+1
        while(len(leftpart)>i):
            a[k]=leftpart[i]
            k=k+1
            i=i+1
        while(len(rightpart)>j):
            a[k]=rightpart[j]
            k=k+1
            j=j+1



a=[]
n=int(input("Enter the Size of the list"))
for i in range(n):
    a.append(random.randrange(1,100))

print(a)
Merge_Sort(a)
print(a)
