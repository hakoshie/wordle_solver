import sys
import nltk
import time
start_time=time.perf_counter()
alphabets="abcdefghijklmnopqrstuvwxyz"
print("input the characters not used in the word >>>",end=" ")
not_used_chars=input()
cand_chars=""
for i in range(len(alphabets)):
    if(alphabets[i] not in not_used_chars):
        cand_chars+=alphabets[i]
print("candidates",cand_chars)
cand_chars=cand_chars.lower()
n=len(cand_chars)
print("input the known characters: apple -> a..le >>>",end=" ")
known_chars=input()
known_chars=list(known_chars)
print("input the hint characters >>>",end= " ")
hints=input()
hints=list(hints)
cand_words=set()
# nltk.download("words")
english_vocab = nltk.corpus.words.words()+list(nltk.corpus.wordnet.words())
english_vocab = set([x.lower() for x in english_vocab if len(x)==5])

arbitrary=["*","."]
def check(word):
    if word.lower() in english_vocab:
        cand_words.add(word)
        return 1
    else:
        return 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                tmp_word=""
                idx=0
                cnt=0
                indices=[i,j,k,l]
                used=[]
                while len(tmp_word)<5:
                    if(known_chars[idx] not in arbitrary):
                        tmp_word+=known_chars[idx]
                        cnt+=1
                    else:
                       tmp_word+=cand_chars[indices[idx-cnt]]
                       used.append(cand_chars[indices[idx-cnt]])
                    idx+=1
                
                if(len(hints)>0):
                    ok=True
                    for m in hints:
                        if(m not in used):
                            ok=False
                            break
                    if(ok):
                        check(tmp_word) 
                    continue
                check(tmp_word)
    # print(i+1,"/",n)
end_time=time.perf_counter()
print(f'{end_time-start_time:.2f}',"seconds")
print("cands = ",cand_words)
if(len(cand_words)>2):
    while(len(cand_words)!=1):
        print("Currently, the number of candidates is ",len(cand_words))
        print("input the character and place to exclude, like n 1 (n is not the first place)","(6 for deleting for all place)")
        print("(6 + place for determined the character's place) >>>")
        try:
            char, place=input().split()
        except:
            sys.exit()
        
        place=int(place)
        cand_drop=set()
        if(place>=7):
            # charの位置がわかっている場合
            for s in cand_words:
                if(s[place-7]!=char):
                    cand_drop.add(s)
        elif(place<=5):
            # charがその位置ではない場合
            for s in cand_words:
                if(s[place-1]==char):
                    cand_drop.add(s)
        else:
            # charが含まれていない場合
            for s in cand_words:
                for j in range(5):
                    if(s[j]==char):
                        cand_drop.add(s)
        cand_words=cand_words-cand_drop
        print(cand_words)
        

        