def MERGE_SORT(A,p,r):
    q = int(0.5*(p + r))
    if p < r:
        MERGE_SORT(A,p,q)
        MERGE_SORT(A,q+1,r)
    return Merge(A,p,q,r)

gurd = 1000

def Merge(A,p,q,r):
    L, R = [],[]
    for i in range(p,q+1):
        L.append(A[i])
    for j in range(q+1,r+1):
        R.append(A[j])
    L.append(gurd)
    R.append(gurd)
    i, j = 0, 0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A

A = [4,9,78,99,100,65,97,237]

print(MERGE_SORT(A,0,len(A)-1))
