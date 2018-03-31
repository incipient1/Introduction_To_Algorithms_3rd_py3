def hoare_partiton(A,p,r):
    x = A[p]
    i = p
    j = r

    while True:
        while A[j] > x:
            j -= 1
        while A[i] < x:
            i += 1

        if i < j:
            A[j], A[i] = A[i], A[j]
        else:
            return j

def quick_sort_hoare(A,p,r):
    if p < r:
        q = hoare_partiton(A,p,r)
        quick_sort_hoare(A,p,q-1)
        quick_sort_hoare(A,q+1,r)
    return A


A = [13,9,5,12,8,7,4,11,2,6,21]
print(quick_sort_hoare(A,0,len(A)-1))