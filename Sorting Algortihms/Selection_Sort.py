import random   # module for gneration random number

def Selection_Sort(a):  #function for Selection_Sort
    for i in range(n):          # it will can scan the whole array
        minimum=min(a[i:])      #it will select the minimum value from the remaining list
        index_of_min=a[i:].index(minimum)+i     #swapping between minimum value
        a[i],a[index_of_min]=a[index_of_min],a[i]



a=[]                #auxilary list for input values
n=int(input("Enter the Size of the list"))
for i in range(n):                          #just generating the
    a.append(random.randrange(1,100))

print(a)
Selection_Sort(a)
print(a)
