def lcs(x,y):
    m=len(x)
    n=len(y)
    c=[[None]*(n+1) for _ in range(m+1)]    
    b=[[None]*n for _ in range(0,m)]
    for i in range(m+1):
        c[i][0]=0
    for j in range(n+1):
        c[0][j]=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]:
                c[i][j]=c[i-1][j-1]+1
                b[i-1][j-1]="d"
            elif c[i-1][j]>=c[i][j-1]:
                c[i][j]=c[i-1][j]
                b[i-1][j-1]="u"
            else:
                c[i][j]=c[i][j-1]
                b[i-1][j-1]="l"
    return (c,b)
def print_lcs(b,x,i,j):
    if i==0 or j==0:
        return
    if b[i-1][j-1]=="d":
        print_lcs(b,x,i-1,j-1)
        print x[i-1],
    elif b[i-1][j-1]=="u":
        print_lcs(b,x,i-1,j)
    else:
        print_lcs(b,x,i,j-1)


x=raw_input('Enter string x:')
y=raw_input('Enter string y:')
len_x=len(x)
len_y=len(y)
(c,b)=lcs(x,y)
print 'Length of lcs is:',c[len_x][len_y]
print 'LCS is:'
print_lcs(b,x,len_x,len_y)
