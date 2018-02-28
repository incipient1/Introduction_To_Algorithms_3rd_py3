def insert_sort(A):
    for i in range(1,len(A)):
        key = A[i]
        j = i - 1
        while j >=0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1

        A[j+1] = key
    return A

if __name__ == '__main__':
    A = [89,32,12,5,6,9,45,19,20,20,16]
    print(insert_sort(A))
