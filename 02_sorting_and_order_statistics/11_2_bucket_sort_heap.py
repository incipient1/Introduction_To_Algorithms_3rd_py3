def build_max_heap(B):
    for j in range((len(B)-2) // 2, -1,-1):
        max_heapify(B,j,len(B)-1)

def max_heapify(B,i,B_heap_size):
    left = 2*i + 1
    right = 2*i +2

    largest = B[i]
    largest_index = i

    if left <= B_heap_size and B[left] > largest:
        largest = B[left]
        largest_index = left

    if right <= B_heap_size and B[right] > largest:
        largest = B[right]
        largest_index = right

    if i != largest_index:
        B[i],B[largest_index] = B[largest_index],B[i]
        max_heapify(B,largest_index,B_heap_size)


def heap_sort(B):
    build_max_heap(B)
    B_length = len(B)
    B_heap_size = B_length -1

    while B_heap_size >= 1:
        B[0],B[B_heap_size] = B[B_heap_size],B[0]
        B_heap_size -= 1
        max_heapify(B,0,B_heap_size)

def bucket_sort_heap(A):
    A_length = len(A)
    B = [[] for _ in range(A_length)]

    for i in range(A_length):
        B[int(A_length * A[i])].append(A[i])

    print(B)

    for i in range(A_length):
        heap_sort(B[i])

    print(B)

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
    print(bucket_sort_heap(A))