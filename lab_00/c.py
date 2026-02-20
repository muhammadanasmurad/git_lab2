pressed = input()
displayed = input()
i = 0
j = 0
silly = ""
wrong = ""
quiet = ""
while i<len(pressed):
    if j<len(displayed) and pressed[i] == displayed[j]:
        i+=1
        j+=1
    else:
        if silly == "" and j<len(displayed):
            silly = pressed[i]
            wrong = displayed[j]
            i+=1
            j+=1
        else:
            quiet = pressed[i]
            i+=1

print(silly,wrong)

if quiet == "":
    print("-")
else:
    print(quiet)
