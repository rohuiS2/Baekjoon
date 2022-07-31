H,M=map(int,input().split())
m=int(input())
if (M+m)>60:
    if H==23:
        print(0,'/n',(M+m)-60)
    else:
        print(H+1,'/n',(M+m)-60)
else:
    print(H,'/n',M+m)
