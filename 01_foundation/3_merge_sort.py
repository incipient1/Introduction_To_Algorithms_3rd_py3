def merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L = list()
    for i in range(p,q+1):
        L.append(A[i])

    R = list()
    for j in range(q+1,r):
        R.append(A[j])

    i = 0
    j = 0
    for k in range(p,r):
        if i == len(L):
            A[k] = R[j]
            j += 1
        elif j == len(R):
            A[k] = L[i]
            i += 1
        elif L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

    return A

def merge_sort(A,p,r):

    if p < r:
        q = int( 0.5*(p+r) )
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)
        return A


A = [2,4,5,7,1,2]
print(merge_sort(A,0,6))
