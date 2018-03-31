def max_heapify(A,i,A_heap_size):
    l = 2*i + 1
    r = 2*i + 2

    if l <= A_heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r <= A_heap_size and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[largest],A[i] = A[i], A[largest]
        max_heapify(A,largest,A_heap_size)

    return A

def build_max_heap(A):
    A_heap_size = len(A)-1
    for i in range((len(A)-2)//2,-1,-1):
        max_heapify(A,i,A_heap_size)

    return A

def heap_sort(A):
    build_max_heap(A)
    A_heap_size = len(A)-1
    for i in range(len(A)-1, 0,-1):
        A[0],A[i] = A[i], A[0]
        A_heap_size = A_heap_size - 1
        max_heapify(A,0,A_heap_size)

    return A

if __name__ == '__main__':
    A = [5,13,2,25,7,17,20,8,4]
    print(heap_sort(A))
