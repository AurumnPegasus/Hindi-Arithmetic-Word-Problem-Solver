fil = open('verbs3 .txt')
data = fil.read()
wrds = data.split()
verbname = []
verbtype = []
for x in range(len(wrds)):
    if(x % 4 == 3):
        verbname.append(wrds[x])
    if(x % 4 == 1):
        verbtype.append(wrds[x])
print(verbname)
print(verbtype)
