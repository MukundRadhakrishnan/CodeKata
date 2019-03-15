CodeKata_pro_n=int(input())
l=[]
for i in range(CodeKata_pro_n):
    l1=input()
    l.append(l1)
CodeKata_pro_a=l[0]
CodeKata_pro_b=l[1]
CodeKata_pro_c=""
CodeKata_pro_r=""
for i in range(len(CodeKata_pro_a)):
    CodeKata_pro_c=CodeKata_pro_c+CodeKata_pro_a[i]
    if CodeKata_pro_c in CodeKata_pro_b:
        CodeKata_pro_r=CodeKata_pro_c
print(CodeKata_pro_r)