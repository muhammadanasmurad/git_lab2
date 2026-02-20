data = int(input("Enter numbrt of data sets: "))
l = []
subject = []
verb = []
objec = []
for num in range(data):
    subject_num = int(input("Enter number of subjects: "))
    verb_num = int(input("Enter number of verbs: "))
    object_num = int(input("Enter number of ovjects: "))
    for i in range(subject_num):
        s = input("Enter subject: ")
        subject.append(s)
    for j in range(verb_num):
        v = input("Enter verb: ")
        verb.append(v)
    for k in range(object_num):
        o = input("Enter object: ")
        objec.append(o)

for i in range(len(subject)):
    for j in range(len(verb)):
        for k in range(len(objec)):
            print(subject[i]+" "+verb[j]+" "+objec[k])
