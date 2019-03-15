codeKata14_a,codeKata14_b=map(int,input().split())
for i in range(codeKata14_a+1,codeKata14_b):
  if i%2!=0 :
    if(i<codeKata14_b):
	    print(i,end=' ')
    else:
      print(i,end="")