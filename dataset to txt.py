
# Writing the dataset in text

filename = 'C:\\Users\\fouad.hannoun\\AppData\\Local\\Packages\\a4548d07-af25-4b98-b7b4-ad4c4798fc82_q8p7fyft9r39a\\LocalState\\Test Folder\\sample.txt'
file = open(filename,'r')
features = []
i=0
j=0
features.append([])
for line in file:
    if (":" not in line):
        features[j].append(float(line.split(" ")[1].strip('\n')))
    i+=1
    if (i==20):
        print(features[j])
        features.append([])
        i=0
        j+=1
del features[-1]


f= open("dataset.txt","w+")
u=0
f.write('[')
for z in features:
    a="["
    for y in z:
        a+=y.strip('\n')+','
    a=a.strip(',')+'],'
    f.write(a)
    u+=1
    if(u==250):
        break
    f.write('\n')
f.write(']')
f.close()

