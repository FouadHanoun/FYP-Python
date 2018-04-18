
''' Writing the dataset in text
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
z=f.read()
f.close()
print(z)
'''
