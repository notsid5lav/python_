def facto(n):
    x=range(1,n+1)

    c=1
    for i in x:
        c=c*i
    return(c)



def addoffac(x,y):
    val1=facto(x)
    val2=facto(y)
    print(x+y)

addoffac(5,20)
