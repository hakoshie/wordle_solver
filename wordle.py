import sys
import nltk
ts="abcdefghijklmnopqrstuvwxyz"
print("input the characters not used in the word >>>",end=" ")
sout=input()
cand_chars=""
for i in range(len(ts)):
    if(ts[i] not in sout):
        cand_chars+=ts[i]
print("candidates",cand_chars)
cand_chars=cand_chars.lower()
n=len(cand_chars)
print("input the known characters: apple -> a**le >>>",end=" ")
known_str=input()
known=list(known_str)
print("input the hint characters >>>",end= " ")
hints=input()
hints=list(hints)
cand=set()
def check(t):
    if len(nltk.corpus.wordnet.synsets(t))!=0:
        cand.add(t)
        return 1
    else:
        return 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                tmp=""
                idx=0
                cnt=0
                indices=[i,j,k,l]
                used=[]
                while len(tmp)<5:
                    if(known[idx]!="*"):
                        tmp+=known[idx]
                        cnt+=1
                    else:
                       tmp+=cand_chars[indices[idx-cnt]]
                       used.append(cand_chars[indices[idx-cnt]])
                    idx+=1
                
                if(len(hints)>0):
                    ok=True
                    for m in hints:
                        if(m not in used):
                            ok=False
                            break
                    if(ok):
                        check(tmp) 
                        continue
                    else:
                        continue
                check(tmp)
print("cands = ",cand)
if(len(cand)>2):
    while(1):
        print("Currently, the number of candidates is ",len(cand))
        print("input the character and place to exclude, like n 1.","(6 for deleting for all place)")
        print("(6 + place for determined a character) >>>")

        try:
            chara, place=input().split()
        except:
            sys.exit()
        
        place=int(place)-1
        deletes=set()
        if(place>=6):
            for s in cand:
                if(s[place-6]!=chara):
                    deletes.add(s)
        elif(place<=4):
            for s in cand:
                if(s[place]==chara):
                    deletes.add(s)
        else:
            for s in cand:
                for j in range(5):
                    if(s[j]==chara):
                        deletes.add(s)
        cand=cand-deletes
        print(cand)
        

        