import os
class stackADT:
    def __init__ (s,n):
        s.n= n
        s.st= [None]*n
        s.top= -1
    def push(s):
        if s.top == s.n-1:
            print("Stack Full\n")
        else:
            s.top+=1
            data=int(input())#"enter the data to be pushed: "
            s.st[s.top]=data
    def display(s):
        for i in range(s.top+1):
            print(s.st[i],end="\n")
    def pop(s):
        if s.top != -1:
            s.top=s.top-1
        else:
            print("Empty Stack")
        
    def peek(s):
            print(s.st[s.top],end="")


n=int(input())
s1=stackADT(n)
q = int(input())
for i in range(q):
    ch=int(input(""))#Enter the option: 
    if ch==1:
        s1.push()
    elif ch==2:
        s1.pop()
    elif ch==3:
        s1.peek()

s1.display()
