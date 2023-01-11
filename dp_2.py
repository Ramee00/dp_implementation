m_score=2
mm_score=-1
S1=''
S2=''
s1="ACACACTA"
s2="AGCACACA"

def match(i,j,arr):
    global S1
    global S2
    S1=s1[i-1]
    S2=s1[i-1]
    return( (arr[i-1][j-1])+m_score)

def mismatch(i,j,arr):
    global S1
    global S2
    if(arr[i][j-1]>arr[i-1][j]):
        S1=s1[i-1]
        S2="_"
    else:
       S1="_" 
       S2=s2[i-1] 
    return( max(arr[i][j-1]+mm_score,arr[i-1][j-1]+mm_score,arr[i-1][j]+mm_score))
    

def DP():
    rows, cols = (9, 9)
    arr = [[0 for i in range(cols)] for j in range(rows)]

    
    for i in range(1,rows):
        for j in range(1,cols):
            #if match
            if(s1[j-1]== s2[i-1]):
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
print()
print(S1)
print(S2)


    