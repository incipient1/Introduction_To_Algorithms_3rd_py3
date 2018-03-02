def bubble_sort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if A[j-1] > A[j]:
                A[j],A[j-1] = A[j-1],A[j]
            else:
                pass
    return A

if __name__ == '__main__':
    A = [2,4,5,7,1,2]
    print(bubble_sort(A))