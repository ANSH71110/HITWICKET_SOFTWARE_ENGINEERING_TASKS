def print_g(grid):
    print('Current Grid:')
    for i in range(5):
        s=''
        for j in range(5):
            if grid[i][j]==[]:
                s+=' - \t'
            else:
                s+=(grid[i][j][1]+':'+str(grid[i][j][0])+'\t')
        print(' '.join(s))


def move(grid,p):
    pl,i=input('Player'+ p +'’s Move:').split(':')
    m=[]
    
    if i=='L':
        m=[0,-1]
        
    elif i=='R':
        m=[0,1]
        
    elif i=='F':
        if p=='A':
            m=[-1,0]
        else:
            m=[1,0]
            
    elif i=='B':
        if p=='A':
            m=[1,0]
        else:
            m[-1,0]
            
    else:
        print('Invalid move')
        move(grid,p)
        
    pl=pl[1:]
    pl=int(pl)
    try:
        indexi=-1
        indexj=-1
        for i in range(5):
            indexi=i
            if [pl,p] in grid[i]:
                indexj=grid[i].index([pl,p])
                break

        if indexj>=0 and indexi>=0 and check_index(indexi+m[0],indexj+m[1],p):
            grid[indexi][indexj]=[]
            #print(grid)
            indexi+=m[0]
            indexj+=m[1]
            grid[indexi][indexj]=[pl,p]
            
        else:
            print('Invalid move')
            move(grid,p)
            
    except:
        print('Invalid move')
        move(grid,p)
        
def check_index(i,j,p):
    if i in range(5) and j in range(5):
        if grid[i][j]!=[]:
            if grid[i][j][1]==p:
                return 0
        return 1
    return 0

def check(grid):
    nb,na=0,0
    for i in range(5):
        for j in range(5):
            if grid[i][j]!=[]:
                if grid[i][j][1]=='B':
                    nb+=1
                else:
                    na+=1

            if nb>0 and na>0:
                return 1
    return 0

  
#main function
if __name__ == '__main__':
    grid=[
            [[2,'B'],[3,'B'],[5,'B'],[4,'B'],[1,'B']],
            [[],[],[],[],[],[]],
            [[],[],[],[],[],[]],
            [[],[],[],[],[],[]],
            [[3,'A'],[2,'A'],[5,'A'],[1,'A'],[4,'A']]
    ]
    print_g(grid)
    i=0
    while check(grid):
        if i%2==0:
            move(grid,'A')
        else:
            move(grid,'B')
        print_g(grid)
        i+=1
