n=int(input("Enter the Number of Items in Room "))
weightOfKnapsack=int(input("Enter the Weight of Knapsack"))
value=[]
weight=[]
for i in range(n):
    value.append(int(input("Enter the Value of item {} : ".format(i+1))))
for i in range(n):
    weight.append(int(input("Enter the Weight of item {} :".format(i+1))))

ratio=[0 for i in range(n)]
for i in range(n):
    ratio[i]=value[i]/weight[i]
for i in range(n):
    for j in range(n-i-1):
        if(ratio[j]<ratio[j+1]):
            ratio[j],ratio[j+1]=ratio[j+1],ratio[j]
            value[j],value[j+1]=value[j+1],value[j]
            weight[j],weight[j+1]=weight[j+1],weight[j]
taking_ratio=[]

for i in range(n):
    if weight[i]<=weightOfKnapsack:
        taking_ratio.append(1)
        weightOfKnapsack=weightOfKnapsack-weight[i]
    else:
        taking_ratio.append(weightOfKnapsack/weight[i])
        weightOfKnapsack=0
        break


total=0
for i in range(len(taking_ratio)):
    total+=(value[i]*taking_ratio[i])
print("The Total Maximum Profit is: {} ".format(total))
