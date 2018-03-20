def selection_sort(a):
    for i in range(len(a)-1):
        min_a = a[i]
        min_index = i
        for j in range(i+1,len(a)):
            if a[j] < min_a:
                min_a = a[j]
                min_index = j

        a[i], a[min_index] = min_a, a[i]

    return a

if __name__ == '__main__':
    a = [89,32,12,5,6,9,45,19,20,20,16]
    print(a)
    print(selection_sort(a))