CodeKata15_a,CodeKata15_b = map(int,input().split())
if CodeKata15_a%2==0 :
	CodeKata15_a = CodeKata15_a+2
else:
	CodeKata15_a=CodeKata15_a+1
if CodeKata15_b%2==0 :
	CodeKata15_b = CodeKata15_b-2
else:
	CodeKata15_b=CodeKata15_b-1
for i in range(CodeKata15_a,CodeKata15_b,2) :
	print(i,end=' ')
print(CodeKata15_b)