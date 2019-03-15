sum = 0
l1=[]
codeKata9,kata9= list(map(int,(input().split())))
for i in range(codeKata9):
    g = int(input("Enter %d  element"%(i)))
    l1.append(g)
for i in range(kata9):
    sum=sum+l1[i]
print(sum)