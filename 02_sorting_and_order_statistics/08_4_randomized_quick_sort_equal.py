import random

def partition_equal(A,p,r):
    x = A[r]
    i = p-1
    k = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j], A[i]
            if A[i] < x:
                k += 1
                A[k],A[i] = A[i], A[k]

    A[i+1],A[r] = A[r], A[i+1]

    return k+1, i+1

def randomized_partition_equal(A,p,r):
    i = random.randint(p,r)
    A[i],A[r] = A[r],A[i]
    return partition_equal(A,p,r)

def randomized_quick_sort_equal(A,p,r):
    if p < r:
        q,t = randomized_partition_equal(A,p,r)
        randomized_quick_sort_equal(A,p,q-1)
        randomized_quick_sort_equal(A,t+1,r)

    return A

A = [2,8,7,1,3,5,6,4,3,3,3,3,3,9,9,9,9,9,8,8,8,1,1,1,1]
p = 0
r = len(A)-1
print(randomized_quick_sort_equal(A,p,r))