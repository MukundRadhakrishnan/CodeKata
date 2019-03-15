import sys, string, math
def CodeKata_reduceFunction( CodeKatapro_n, CodeKatapro_k) :
	if CodeKatapro_k <= 0 : return CodeKatapro_n
	if CodeKatapro_n == 0 : return 10
	p1 = CodeKata_reduceFunction(CodeKatapro_n//10, CodeKatapro_k)*10 + CodeKatapro_n%10
	p2 = CodeKata_reduceFunction(CodeKatapro_n//10, CodeKatapro_k-1)
	if p1 < p2 :
		return p1
	else :
		return p2
CodeKatapro_n,CodeKatapro_k = input().split()
CodeKatapro_n,CodeKatapro_k = int(CodeKatapro_n),int(CodeKatapro_k)
print(CodeKata_reduceFunction(CodeKatapro_n,CodeKatapro_k))