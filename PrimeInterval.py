CodeKata16_a,CodeKata16_b = map(int,input().split())
CodeKata16_a = CodeKata16_a+1
L = []
for i in range(CodeKata16_a,CodeKata16_b) :
	for j in range(2,i) :
		if i%j == 0 :
			break
	else :
		L.append(i)
print(*L)