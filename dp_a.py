m_score=2
mm_score=-1

def match(i,j,arr):
    return( (arr[i-1][j-1])+m_score)

def mismatch(i,j,arr):
    return( max(arr[i][j-1]+mm_score,arr[i-1][j-1]+mm_score,arr[i-1][j-1]+mm_score))
    

def DP():
    rows, cols = (3, 3)
    arr = [[0 for i in range(cols)] for j in range(rows)]
    """for i in range(0,cols+1):
        arr[i][0]=0;
    for j in range(0,rows+1):
            arr[0][j]=0;"""
    s1="AC"
    s2="AG"
    
    for i in range(1,rows):
        for j in range(1,cols):
            #if match
            if(s1[i-1]== s2[j-1]):
                arr[i][j]=match(i,j,arr)
            #not a match
            else:
                arr[i][j]=mismatch(i,j,arr)
    print()
    for i in range(0,rows):
        for j in range(0,cols):
            print(arr[i][j], end = " ")
        print()
    
DP()