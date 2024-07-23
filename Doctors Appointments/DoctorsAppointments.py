

def patientfunc2(di):
    places=[]
    pa=[]
    for i, key in enumerate(di.keys()):
        # print(i, di[key])
        for place,j in enumerate(di[key]):
            if j==1 and (place+1) not in places:
                pa.append(key)
                places.append(place+1)
                break
            else:
                continue
    # print(*pa)
    if len(pa)==patients:
        print (*pa)
    else:
        print("impossible")



testCases=  int(input().strip())
for i in range(testCases):
    days=[]
    patients=int(input().strip())
    
    L={}
    count = {}
    for p in range(1,patients+1):
        patientCount=[0]*patients
        Li,Ri = map(int,input().split())
        patientCount[Li-1:Ri]=[1]*(Ri-Li +1)
        L[p] = patientCount
        count[p] = Ri-Li+1
    count = dict(sorted(count.items(), key=lambda item: item[1]))
    sort_patient = {}
    for key in count.keys():
        sort_patient[key] = L[key]
    patientfunc2(sort_patient)
 