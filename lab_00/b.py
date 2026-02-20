num = int(input("Number of codes? "))
l1=[]
for i in range(num):
    code = input("Enter the code: ")
    l1.append(code)
retur = []
for code in l1:
    n = list(code)
    aplha = ""
    num = 0
    for i in n:
        if i.isalpha and i.isupper():
            aplha+=i
        elif i.isdigit():
            num+=abs(int(i))
    final = aplha + str(num)
    retur.append(final)
            
for i in retur:
    print(i)
    