heros=['spider man','thor','hulk','iron man','captain america']

print("The number of Heroes is ", len(heros))
heros.append('black panther')
print("The Heroes in the list ", heros, sep='\n')
heros.remove('black panther')
k=0
for i in range(len(heros)):
    if heros[i] == 'hulk':
        k=i
        break;
heros.insert(k+1,'black panther')
print("The Heroes in the list ", heros, sep='\n')
heros.remove('hulk')
heros.remove('thor')
heros.append('doctor strange')
print("The Heroes in the list ", heros, sep='\n')
heros.sort()
print("The Heroes in the list ", heros, sep='\n')