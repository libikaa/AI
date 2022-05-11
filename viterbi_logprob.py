h = {"a":-2.322,"c":-1.737,"g":-1.737,"t":-2.322,"h":-1,"l":-1}
l = {"a":-1.737,"c":-2.322,"g":-2.322,"t":-1.737,"l":-0.737,"h":-1.322}

startH = -1
startL = -1

pattern = "ggcactgaa"

hp = [startH+h[pattern[0]]]
lp = [startL+l[pattern[0]]]

most_likely_seq=[]    

for pat in pattern[1:]:
    xh = h[pat] + max(hp[-1]+h['h'] , lp[-1]+l['h'])
    xl = l[pat] + max(hp[-1]+h['l'] , lp[-1]+l['l'])
    
    hp.append(xh)
    lp.append(xl)


def printPath():
    count=[0,0]

    for i in range(len(lp)):
        maximum=max(hp[i],lp[i])
        if(maximum==hp[i]):
            count[0]+=1
            most_likely_seq.append('H')
        else:
            count[1]+=1
            most_likely_seq.append('L')

    if count[0]>count[1]:
        s='H'
    else:
        s='L'
        
    print("The most likely sequence of states that genertated",pattern,"is :",s)
    print(most_likely_seq)
            

print(2**max(lp[-1],hp[-1]))

printPath()