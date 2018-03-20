import random

def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[j],A[i] = A[i],A[j]

    A[i+1],A[r] = A[r],A[i+1]
    return i+1

def randomized_partition(A,p,r):
    k = random.randint(p,r)
    A[r],A[k] = A[k],A[r]
    return partition(A,p,r)

def randomized_quick_sort(A,p,r):
    if p < r:
        q = randomized_partition(A,p,r)
        randomized_quick_sort(A,p,q-1)
        randomized_quick_sort(A,q+1,r)

    return A

A = [12,2,8,7,1,3,5,6,4,9,10,11]
p = 0
r = len(A)-1
print(randomized_quick_sort(A,p,r))