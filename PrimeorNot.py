import sys
CodeKata_13_a=int(input())
if CodeKata_13_a==1:
    print("no")
elif CodeKata_13_a==2 or CodeKata_13_a==3: 
    print("yes")
else:
    for i in range(2,CodeKata_13_a):
        if CodeKata_13_a%i==0:
            print("no")
            sys.exit()
    else:
            print("yes")