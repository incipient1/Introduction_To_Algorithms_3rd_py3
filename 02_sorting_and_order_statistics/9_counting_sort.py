def counting_sort(A):
    k = A[0]
    A_length = len(A)
    for i in A:
        if i > k:
            k = i

    B = [0 for _ in A]
    print(B)
    C = [0 for _ in range(k+1)]
    print(C)

    for j in range(A_length):
        C[A[j]] += 1

    for j in range(1,k+1):
        C[j] = C[j] + C[j-1]

    print(C)

    for j in range(A_length-1, -1, -1):
        B[C[A[j]]] = A[j]
        C[A[j]] -= 1

    return B

A = [6,0,2,0,1,3,4,6,1,3,2]
print(counting_sort(A))