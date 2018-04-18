import time
from sklearn.datasets import make_regression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split



'''                                                   ----             FEATURES            ----


HeadBackward HeadBentForward HeadOnHand_Left HeadOnHand_RightHandOnHead_Left HandOnHead_Right SpineForward SpineBackward ShouldersForward ShouldersRaisedArmsAtTrunk
ArmsRaisedShoulder HandsOnKnees CrossedArms ArmsRaisedUp ArmsExtendedDown HandsBehindHead HandOnNeck_Left HandOnNeck_Right


'''

def fill(p,n):
    fx=open(n,'r')
    x=[]
    j=0
    for l in fx:
        x.append([])
        l=l.split(" ")
        for i in range (0,p):
            x[j].append(float(l[i]))
        j+=1
    fx.close()
    return x

X=fill(19,"X.txt")
y=fill(3,"Y.txt")

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
        features.append([])
        i=0
        j+=1
del features[-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
k=MultiOutputRegressor(GradientBoostingRegressor(random_state=0)).fit(X, y).predict(features)

for i in k:
    if(i[0]>60): print("neutre")
    if(i[1]>60): print("heureux")
    if(i[2]>60): print("triste")
    
'''for i in range (0,50):
    print(mean_absolute_error(y_test[i], k[i]))'''
