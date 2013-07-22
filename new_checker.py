# 5 X 5 CHECKER BOARD

cost_arr=[[0,0,0,0,0,0],[0,8,81,80,4,9],[0,1,2,7,100,3],[0,5,11,1,20,6],[0,10,7,60,4,2],[0,8,120,6,5,3]]
path_arr=[[0]*7 for _ in range(7)]
profit_arr=[[0]*7 for _ in range(7)]

def max_profit():
    n=len(cost_arr)
    global path_arr
    global profit_arr
    
    for i in range(1,n):
        profit_arr[1][i]=cost_arr[1][i]
    
    for i in range(2,n):
        for j in range(1,n):
            m=max(profit_arr[i-1][j-1],profit_arr[i-1][j],profit_arr[i-1][j+1])
            profit_arr[i][j]=m+cost_arr[i][j]
            if m==profit_arr[i-1][j-1]:
                path_arr[i][j]=-1
            elif m==profit_arr[i-1][j]:
                path_arr[i][j]=0
            else:
                path_arr[i][j]=1


def comp_path():
    global profit_arr
    n=len(cost_arr)-1
    max_profit()
    max_ind=1
    max_pro=profit_arr[n][1]
    for i in range(2,n):
        if profit_arr[n][i]>max_pro:
            max_ind=i
            max_pro=profit_arr[n][i]
    print 'Maximum profit:',max_pro
    print 'Path traversed is:'
    print_path(n,max_ind)
    

def print_path(i,j):
    global path_arr
    print 'column',j,
    print '<-',
    if i==2:
        print 'column',j+path_arr[i][j],
        return
    else:
        print_path(i-1,j+path_arr[i][j])



#print p

#print q
print '5 X 5 checker board'
n=len(cost_arr)
for i in range(1,6):
    for j in range(1,6):
        print cost_arr[n-i][j],'  ',
    print '\n'
comp_path()
    
                
