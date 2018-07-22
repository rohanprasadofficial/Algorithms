
"""
Author  :  Rohan Prasad
Date  : 2/3/2018
Problem : Activity Selection Problem (Greedy Algorithms)
"""

n=int(input("Enter the number of Activities "))

s=[]
f=[]


for i in range(n):
    elem=int(input("Enter the  Start  time of task {}".format(i)))
    s.append(elem)
for i  in range(n):
    elem=int(input("Enter the  Finish time of  taks  {} ".format(i)))
    f.append(elem)

a={0}
j=1

for i in range(n):
    for j in range(n-1-i):
        if(f[j+1]<f[j]):
            temp=f[j+1]
            f[j+1]=f[j]
            f[j]=temp
            temp=s[j+1]
            s[j+1]=s[j]
            s[j]=temp




#print(f)
#print(s)

for i in range(1,n):
    if(f[j] <= s[i]):
        a=a|set([i])
        j=i

print("The Task Performed are  :")
print(a)
