def cir_shift(a,n):
        temp2=a[0]
        for i in range(n-1):
                temp1=temp2
                temp2=a[i+1]       
                a[i+1]=temp1
        a[0]=temp2
        
#q=input("Enter NO. of times : ")
for i in range(1):
        l=input("Enter Numbers\nFrom: ")
        r=input("TO: ")
        n=[]
        sol=[]
        u=len(list(str(r)))
        for j in range(r):
                if j<=u:
                        if j!=0:
                                n.append(j)
                else:
                        break
        print n
        for j in range(u):
                nu=[]
                for k in range(j+1):
                        if n[k]<=j+1 :
                                nu.append(n[k])
                for k in range(j+1):
                        ans=int(''.join(str(e) for e in nu))
                        if ans>=l and ans<=r:
                                sol.append(ans)
                        cir_shift(nu,j+1)
        print sol
        print("ToTal AlMighty NumBer BeTween EnterEd RanGe Is: %d"%len(sol))
