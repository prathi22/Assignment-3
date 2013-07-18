#Matrix multiplication using dynamic programming

def mat_mul(p):
    n=len(p)-1
    m=[[None]*n for _ in range(n)]
    s=[[None]*n for _ in range(n)]
    for i in range(n):
        m[i][i]=0
    for l in range(1,n):
        for i in range(n-l):
            j=i+l
            m[i][j]=float("inf")
            for k in range(i,j):
                q=m[i][k]+m[k+1][j]+p[i]*p[k+1]*p[j+1]
                if q<m[i][j]:
                    m[i][j]=q
                    s[i][j]=k
    return (m,s)

def opt_paren(s,i,j):
    if i==j:
        print 'A',i+1,
    else:
        print '(',
        opt_paren(s,i,s[i][j])
        opt_paren(s,s[i][j]+1,j)
        print ')',

n=int(raw_input('Enter the no. of matrices'))
print 'Enter a sequence of orders of matrices'
p=[]
for i in range(n+1):
    p.append(int(raw_input()))

(m,s)= mat_mul(p)
print 'Minimum cost',m[0][n-1]
print 'k value',s[0][n-1]+1
print 'Matrices parenthesization:'
opt_paren(s,0,n-1)


    
