
def orangecap(d):
    players, scores = [], []
    for key, matchs in d.items():
        l = zip(matchs.values(), matchs.keys())
        for a, b in l:
            players.append(b)
            scores.append(a)

    res = []
    index, aindex = [], []
    for (i, value) in enumerate(players): 
        if value not in res: 
            res.append(value)
            c = players.index(value)
            aindex.append(c)
            continue
        index.append(i)

    for i in index:
        for j in aindex:
            if players[i] == players[j]:
                scores[j] = scores[j] + scores[i]

    index.reverse()
    for i in index:
        scores.pop(i)

    a, b = tuple(res), tuple(scores)
    m = max(zip(b, a))
    p = (m[1], m[0])

    return p

def addpoly(p1,p2):
    result=[]
    i1,i2=0,0
    l1,l2=len(p1),len(p2)
    while(i1<l1 and i2<l2):
        if(p1[i1][1]>p2[i2][1]):
            result.append(p1[i1])
            i1+=1
        elif(p1[i1][1]<p2[i2][1]):
            result.append(p2[i2])
            i2+=1
        else:
            if(p1[i1][0]+p2[i2][0]!=0):
                result.append((p1[i1][0]+p2[i2][0],p1[i1][1]))
            i1+=1
            i2+=1
    while(i1<l1):
        result.append(p1[i1])
        i1+=1
    while(i2<l2):
        result.append(p2[i2])
        i2+=1
    return result

def multpoly(p1,p2):
    result_dict=dict()
    for coeff1,exp1 in p1:
        for coeff2,exp2 in p2:
            try:
                result_dict[exp1+exp2] += coeff1*coeff2
            except:
                result_dict[exp1+exp2] = coeff1*coeff2
    return sorted([(coeff,exp) for exp,coeff in result_dict.items() if coeff!=0],key=lambda x: x[1],reverse=True)