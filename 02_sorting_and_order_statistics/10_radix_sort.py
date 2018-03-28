def digit_i(A,i):
    return [j % (10*i) // i for j in A]

def counting_sort(A,A1):
    C = [0 for _ in range(10)]
    B = [0 for _ in A1]

    A1_length = len(A1)
    for j in range(A1_length):
        C[A1[j]] += 1

    for j2 in range(1,10):
        C[j2] += C[j2-1]

    for j3 in range(A1_length-1,-1,-1):
        B[C[A1[j3]]-1] = A[j3]
        C[A1[j3]] -= 1

    return B

def radix_sort(A):
    digit = len(str(max(A)))
    for i in range(digit):
        A1 = digit_i(A,10**i)
        A = counting_sort(A,A1)

    return A

if __name__ == '__main__':
    A = [329,457,657,839,436,720,355,23,34,1000,1,987,0,1000]
    print(radix_sort(A))