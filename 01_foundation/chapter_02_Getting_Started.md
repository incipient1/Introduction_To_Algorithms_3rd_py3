
# 第2章 算法基础

## 2.1插入排序

### 2.1练习

#### 2.1-1 以图为模型，说明INSERT_SORT在数组A=[31,41,59,26,41,58]上的执行过程

1. 第1次for循环，已经排序完成的是A=[31]，取key = A[1]，即41。while循环开始时，j=0，A[0]=31，A[0] \< A[1]，循环开始条件不具备，循环结束。赋值A[j+1] = key。  
2. 第2次for循环，已经完成的排序是A=[31,41],key = A[2]，即59。while循环开始时，j=1，A[j]=A[1]=41，41\<59，循环开始条件不具备，循环结束。赋值A[j+1] = key = 59  
3. 第3次for循环，已经完成的排序是A=[31,41,59],key = A[3]，即26。while循环开始时，j=2，A[2]=59，A[2] > 26，循环开始条件具备，A[j+1] = A[j]，即A[3] = 59；j=j-1=1，开始第2次while循环。A[1] = 41 > 26，A[j+1] = A[j]，即A[2] = 41；j=j-1=0，开始第3次while循环，A[0] = 31 > 26，A[j+1] = A[j]，即A[1] = 31；j=j-1=-1\<0，while循环结束。赋值A[j+1] = key，即A[0] = 26

#### 2.1-2 重写insert_sort，使之按照非升序排序


```python
def insert_sort_noincrease(A):
    for i in range(1,len(A)):
        key = A[i]
        j = i - 1
        while (j>=0) and (A[j] <= key):
            A[j+1] = A[j]
            j -= 1
            
        A[j+1] = key
    return A

if __name__ == '__main__':
    A = [89,32,12,5,6,9,45,19,20,20,16]
    print(insert_sort_noincrease(A))
```

    [89, 45, 32, 20, 20, 19, 16, 12, 9, 6, 5]
    

#### 2.1-3 查找问题


```python
def searching(A,v):
    for i in range(len(A)):
        if A[i] == v:
            return i
            break
        else:
            pass
    
    return 'NIL'

if __name__ == '__main__':
    A = [89,32,12,5,6,9,45,19,20,20,16]
    v = 16
    print(searching(A,v))
```

    10
    

循环终止有两种情况：<br>
1. 找到了i，使得A[i]等于v，这时返回下标i
2. for循环解除，即表明没有找到，这是返回'NIL'

####  2.1-4 两个n位二进制整数相加整数相加

**输入：**n位二进制整数A、B<br>
**输出：**n+1位的二进制整数C，C等于A、B之和


```python
def binary_sum(a,b):
    c = list()
    for _ in range(len(a)+1):
        c.append(0)
#     print('数组c长度：',len(c))
    
    for i in range(len(a)-1,-1,-1):
        c[i], c[i+1] = divmod((a[i] + b[i] + c[i+1]),2)
    
    return c

if __name__ == '__main__':
    a = [0,1,1,1,1,1,1,0,0,1,1]
    b = [0,0,1,1,0,0,1,0,0,1,1]
    print('数组a长度：',len(a))
#     print('  ',a)
#     print('  ',b)
    print(binary_sum(a,b))
```

    数组a长度： 11
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0]
    

## 2.2分析算法

### 2.2练习

#### 2.2-1&ensp;用$\Theta$记号表示函数$n^{3}/1000-100n^{2}-100n+3$

$\Theta (n^{3})$

#### 2.2-2&ensp;选择排序


```python
def selection_sort(a):
    for i in range(len(a)-1):
        min_a = a[i]
        min_index = i
        j = i+1
        for j in range(i+1,len(a)):
            if a[j] < min_a:
                min_a = a[j]
                min_index = j
            else:
                pass
        
        a[i], a[min_index] = min_a, a[i]
    
    return a

if __name__ == '__main__':
    a = [89,32,12,5,6,9,45,19,20,20,16]
#     print(a)
    print(selection_sort(a))
```

    [89, 32, 12, 5, 6, 9, 45, 19, 20, 20, 16]
    [5, 6, 9, 12, 16, 19, 20, 20, 32, 45, 89]
    

**循环不变式是：**前j-1个数是已经排好序的<br>
**循环只到前n-1个元素：**因为第n个元素是和n-1元素交换后的较大值<br>
**最好情况：**已经排好序了，总次数为$\Theta (n^{2})$，计算过程：$\begin{equation*}
\sum\limits_{i=1}^{n-1}[5+\sum\limits_{j=i+1}^{n}(n-j+1)]
\end{equation*}$<br>
**最坏情况：**逆序，总次数$\Theta (n^{2})$，计算过程：$\begin{equation*}
\sum\limits_{i=1}^{n-1}[5+\sum\limits_{j=i+1}^{n}(n-j+3)]
\end{equation*}$<br>

#### 2.2-3&ensp;线性查找问题

**平均情况：**$\Theta(n)$，因为假设元素是平均分布的，查找的期望运行次数是$\frac{n}{2}$<br>
**最坏情况：**$\Theta(n)$，假设查抄了所有元素，但是都没有找到，运行次数是$2n$

## 2.3&ensp;设计算法

### 2.3&ensp;练习

#### 2.3-1&ensp;说明归并排序在数组A=[3,41,52,26,38,57,9,49]上的操作

1. 
