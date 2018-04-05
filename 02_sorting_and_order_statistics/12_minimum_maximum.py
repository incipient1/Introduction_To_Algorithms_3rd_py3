def min_max(A):
    A_length = len(A)
    max_index = 0

    if A_length %2 == 0:
        if A[0] < A[1]:
            min_a,max_a = A[0],A[2]
        else:
            min_a,max_a = A[1],A[0]

        max_index = 1

    else:
        min_a,max_a = A[0],A[0]


    for j in range(max_index+1,len(A),2):
        if A[j] < A[j+1]:
            if A[j] < min_a:
                min_a = A[j]

            if A[j+1] > max_a:
                max_a = A[j+1]

        else:
            if A[j+1] < min_a:
                min_a = A[j+1]

            if A[j] > max_a:
                max_a = A[j]

    return min_a,max_a

if __name__ == '__main__':
    A = [1,-2,3,190,0,1,3,4,6,7]
    print(len(A))
    print(min_max(A))