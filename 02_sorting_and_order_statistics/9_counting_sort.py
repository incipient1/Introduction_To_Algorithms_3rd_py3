def counting_sort(A):
    k = A[0]
    A_length = len(A)
    for i in A:
        if i > k:
            k = i

    B = [0 for _ in A]
    C = [0 for _ in range(k+1)]

    for j1 in range(A_length):
        C[A[j1]] += 1

    for j2 in range(1,k+1):
        C[j2] = C[j2] + C[j2-1]

    for j3 in range(A_length-1, -1, -1):
        B[C[A[j3]]-1] = A[j3]
        C[A[j3]] -= 1

    return B

A = [6,0,2,0,1,3,4,6,1,3,2]

print(counting_sort(A))