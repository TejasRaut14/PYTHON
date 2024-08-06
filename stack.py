l=[]
while True:
    c=int(input('''
       1  push elements
       2  pop elements
       3  Peek elements
       4  display stack 
       5  exit 
       '''))
    if c==1:
        n=input("enter the value")
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("empty stack")
        else:
         q=l.pop()
        print(q)
        print(l)
    elif c==3:
        if len(l)==0:
            print("empty stack")
        else:
            print("last stack value",l[-1])
    elif c==4:
             print("display stack",l)
    elif c==5:
          print("exit")
