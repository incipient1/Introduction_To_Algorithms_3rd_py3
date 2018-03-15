
# 第6章&ensp;堆排序

## 6.1&ensp;堆排序

### 6.1&ensp;练习

#### 6.1-2&ensp;高度为h的堆，元素最多和最少为？

1. 元素最多为：$2^{h+1}-1$个，此时堆是完全充满的
1. 元素最少为：$2^{h}$个，此时最下面一层只有一个元素

#### 6.1-2&ensp;证明含n个元素的堆的高度为$\lfloor lgn \rfloor$

高度为h的堆，最少元素$2^h$个，$2^h \leqslant n$，h最大为lgn，h又为整数，所以h为$\lfloor lgn \rfloor$

#### 6.1-3&ensp;**最大堆**的任一子树，该子树包含的最大元素在根节点上

在最大堆中，除根节点外对任一节点i，A[parent(i)] >= A[i]，而根节点没有parent，所以根节点中的元素是最大元素（之一）

#### 6.1-4&ensp;该堆的最小元素在？

在没有子节点的那些节点中

#### 6.1-5&ensp;一个已排好序的数组是最小堆吗？

是

#### 6.1-6&ensp;是最大堆吗？

不是，元素6的页节点元素为5、7

#### 6.1-7&ensp;证明叶节点下标

n为叶节点，n的根节点为n/2（n为偶数时，属于左孩子）或者(n-1)/2(n为奇数时，右孩子)，即$\lfloor n/2 \rfloor$，此节点右边的节点即全部为叶节点，直至n，所以叶节点的下标为$\lfloor n/2 \rfloor,\lfloor n/2 \rfloor+1,...,n-1,n$

## 6.2&ensp;维护堆的性质

### 6.2&ensp;练习

#### 6.2.-1&ensp;模仿图6-2



#### 6.2-2&ensp;最小堆伪码


```python
def left(i):
    return 2*i +1

def right(i):
    return 2*i + 2

def parent(i):
    if (i-1)//2 >= 0:
        return (i-1)//2
    else:
        return 'NIL'
    
def MIN_HEAPIFY(A,i):
    l = left(i)
    r = right(i)
    if l <= len(A) and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r <= len(A) and A[r] < A[smallest]:
        samllest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        MIN_HEAPIFY(A,smallest)
    return A

A = [27,17,3,16,13,10,1,5,7,12,4,8,9,0]
print(MIN_HEAPIFY(A,0))
```

    [17, 16, 3, 5, 13, 10, 1, 27, 7, 12, 4, 8, 9, 0]
    

运行时间相同

#### 6.2-3&ensp;结果

做1次比较运算后结束，整个堆不发生任何变化

#### 6.2-4&ensp;结果

largest = i,递归结束

#### 6.2-5&ensp;循环结构的MAX_HEAPIFY


```python
def left(i):
    return 2*i +1

def right(i):
    return 2*i + 2

def max_heapify(A,i):
    largest = i
    l = left(i)
    r = right(i)
    A_heap_size = len(A)-1
    while l <= A_heap_size:
        if A[l] > A[i]:
            largest = l
        if r <= A_heap_size and A[r] > A[largest]:
            largest = r
            
        if largest != i:
            A[i],A[largest] = A[largest], A[i]
            i = largest
            l = left(i)
            r = right(i)
        else:
            break
    
    return A

A = [27,17,3,16,13,1,1,5,7,9,4,8,9,2]
print(A)
print(list(range(14)))
print(max_heapify(A,8))
```

    [27, 17, 3, 16, 13, 1, 1, 5, 7, 9, 4, 8, 9, 2]
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    [27, 17, 3, 16, 13, 1, 1, 5, 7, 9, 4, 8, 9, 2]
    

#### 6.2-6&ensp;证明

最坏运行情况举例：从根节点到叶节点路径上每个节点都会递归调用MAX_HEAPIFY，调用的总次数为$lgn$，每次运行时又要消耗常数时间，故最坏运行时间为$\Omega(lgn)$

## 6.3&ensp;建堆

### 6.3&ensp;练习

#### 6.3-1&ensp;模仿图6-3

#### 6.3-2&ensp;why？

第一次for循环开始时，以i+1、i+2……、n为根节点的堆是最大堆，循环结束，以i为根节点的堆也是最大堆<br>
第二次for循环开始时，以i+1、i+2……、n为根节点的堆仍是最大堆<br>
循环结束，i=0，此时以i+1、i+2……、n为根节点的堆仍是最大堆！并且A[0]是堆中的最大值<br>
假设从1递增到$\lfloor A.length/2 \rfloor$，无法建立循环不变量

#### 6.3-3&ensp;证明

## 6.4&ensp;堆排序算法

### 6.4&ensp;练习

#### 6.4-1&ensp;仿照图6-4

已仿照，然后才写出了heap_sort的代码

#### 6.4-2&ensp;分析heap_sort循环不变量的正确性

第一次迭代开始，i=n，此时数组A[1...n]是一个包含了第n小（即最大）元素的最大堆（由第1行代码实现），数组A[n+1]为空；<br>
第3行代码，将A[1]（A[1]是A[1....n]中的最大值之一）与A[n]交换；第4行代码，将A[n]（交换后，为最大值之一）排除到最大堆有效元素之外；第5行代码，维护堆，使A[1....n-1]仍然是最大堆；<br>
第二次迭代开始，i=n-1，此时数组A[1....n-1]是一个包含了第n-1小元素的最大堆<br>
迭代结束，i= 0

#### 6.4-3&ensp;升序、降序时，heap_sort时间复杂度？

均为$\Theta(nlgn)$
