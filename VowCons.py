list=['a','e','i','o','u']
list2=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
CodekataExample3=input()
if(CodekataExample3 in list):
    print("Vowel")
elif(CodekataExample3 in list2):
    print("Consonant")
else:
    print("invalid")