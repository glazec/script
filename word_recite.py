import random
dict={'appreciate':'gerunds',
'avoid':'gerunds',
'anticipate':'gerunds',
'complete':'gerunds',
'consider':'gerunds',
'delay':'gerunds',
'deny':'gerunds',
'discuss':'gerunds',
'dislike':'gerunds',
'enjoy':'gerunds',
'finish':'gerunds',
'keep':'gerunds',
'involve':'gerunds',
'mention':'gerunds',
'mind':'gerunds',
'miss':'gerunds',
'practice':'gerunds',
'quit':'gerunds',
'recommend':'gerunds',
'suggest':'gerunds',
'tolerate':'gerunds',

'appologize':'appologize for',
'plan':'plan on',
'put':'put off',

'agree':'infinite',
'afford':'infinite',
'ask':'infinite',
'decide':'infinite',
'demand':'infinite',
'expect':'infinite',
'have':'infinite',
'hope':'infinite',
'intend':'infinite',
'invite':'infinite',
'learn':'infinite',
'manage':'infinite',
'need':'infinite',
'offer':'infinite',
'order':'infinite',
'plan':'infinite',
'pretend':'infinite',
'remind':'infinite',
'seem':'infinite',
'tell':'infinite',
'want':'infinite',
'warn':'infinite'}
correct=0
incorrect=0
while dict:
    a=list(dict.keys())[random.randrange(len(list(dict.keys())))]
    print(a)
    b=input("write the answer:\n")
    c=dict.get(a)
    if b in c:
        print("correct\n")
        correct+=1
        dict.pop(a)
        print(str(len(list(dict.keys())))+" left")
    else:
        print(a,"+",c)
        incorrect+=1
rate=incorrect/(correct+incorrect)
print("finish\nscore: ",rate)
