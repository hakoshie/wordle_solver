import sys
import nltk
ts="abcdefghijklmnopqrstuvwxyz"
print("input the characters not used in the word >>>",end=" ")
sout=input()
s=""
for i in range(len(ts)):
    if(ts[i] not in sout):
        s+=ts[i]
print("candidates",s)
s=s.lower()
n=len(s)
print("input the known characters: apple -> a**le >>>",end=" ")
known_str=input()
known=list(known_str)
print("input the hint characters >>>",end= " ")
restrict=input()
restrict=list(restrict)
# for i in range(len(restrict)):
#     resnums.append(ord(restrict[i])-ord("a"))
def check(t):
    if len(nltk.corpus.wordnet.synsets(t))!=0:
        cand.add(t)
        return 1
    else:
        return 0
cand=set()
for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                t=""
                idx=0
                nums=[i,j,k,l]
                used=[]
                cnt=0
                while len(t)<5:
                    if(known[idx]!="*"):
                        t+=known[idx]
                        cnt+=1
                    else:
                        t+=s[nums[idx-cnt]]
                        used.append(s[nums[idx-cnt]])
                    idx+=1
                
                if(len(restrict)>0):
                    ok=True
                    for m in restrict:
                        if(m not in used):
                            ok=False
                            break
                    if(ok):
                        check(t) 
                        continue
                    else:
                        continue
                check(t)
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
        

        