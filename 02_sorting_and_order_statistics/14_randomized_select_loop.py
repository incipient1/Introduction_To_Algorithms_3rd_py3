import random

def randomized_select(A,p,r,i):
    while p < r:
        q = randomized_partition(A,p,r)
        k = q-p+1

        if i == k:
            return A[q]
        elif i < k:
            r = q-1
        else:
            i -= k
            p = q+1

    else :
        if p == r:
            return A[p]

def randomized_partition(A,p,r):
    i = random.randint(p,r)
    A[i],A[r] = A[r],A[i]
    return partition(A,p,r)

def partition(A,p,r):
    x = A[r]
    i = p-1

    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j],A[i]

    A[i+1],A[r] = A[r],A[i+1]
    return i+1

if __name__ == '__main__':
    A = [12,34,56,98]
    print(randomized_select(A,0,len(A)-1,3))