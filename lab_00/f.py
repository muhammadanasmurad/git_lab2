x = int(input("Enter number of gathered persons: "))
l=[]
for i in range(x):
    hat = int(input("Enter each person's hat no. clockwise: "))
    l.append(hat)

count = 0

for i in range(len(l)):
    if l[i] == l[(i+x//2)%x]:
        count+=1
        continue
print(count)
    