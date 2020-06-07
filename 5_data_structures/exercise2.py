from pprint import pprint
sentence = "find the most repeated word in this phase"
char_freq ={} #creating dectionary
for x in sentence:
    if x in char_freq:
        char_freq[x] +=1
    else:
        char_freq[x] = 1
# pprint(char_freq,width=2)
arranging = sorted(char_freq.items(),key=lambda kv:kv[1],reverse=True)
print(arranging)
print(arranging[0])