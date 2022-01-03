from random import*
def insert(t):
    n=len[t]
    for i in range(n-1):
        x=t[i]
        j=i
        while j>0 and x<t[j-1]:
            t[j]=t[j-1]
            j=j-1
        t[j]=x
    print (t[j])

def selec(t):
    len[t]
    for i in range(n-1):
        min=t[i]
        imin=i
        for j in range(i+1,n-1):
            if t[j]<min:
                min=t[j]
                imin=j
        a=t[i]
        t[i]=imin
        imin=a




def ttc(n,d):
    t=[0]*n
    for i in range(n-1):
        t[i+1]=t[i]+randint(0,d)
    return t

def copie(t):
    c=[0]*len(t)
    for i in range(len(t)):
        c[i]=t[i]
    return c

def test_tri():
    for n in range(100):
        t1= ttc(n,0)
        t2=ttc(n,n//5)
        t3=ttc(n,5*n**2)
        c1,c2,c3=copie(t1),copie(t2),copie(t3)
        shuffle(t1)
        shuffle(t2)
        shuffle(t3)
        selec(t1)
        selec(t2)
        selec(t3)
        assert t1==c1
        assert t2==c2
        assert t3==c3
    print ("tout va bien")
    
    
    
    
    
    
    
    






