def insert_sort(A):
    for i in range(len(A)):
        key = A[i]
        j = i-1

        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        else:
            A[j+1] = key


def bucket_sort(A):
    A_length = len(A)
    B = [[] for _ in range(A_length)]

    for i in range(A_length):
        B[int(A_length * A[i])].append(A[i])

    for i in range(A_length):
        insert_sort(B[i])

    C = []
    for i in B:
        if isinstance(i,list):
            for j in i:
                C.append(j)
        elif i is not None:
            C.append(i)
        else:
            pass

    return C

if __name__ == '__main__':
    A = [0.78,0.13,0.16,0.64,0.39,0.2,0.89,0.53,0.71,0.42]
    print(bucket_sort(A))