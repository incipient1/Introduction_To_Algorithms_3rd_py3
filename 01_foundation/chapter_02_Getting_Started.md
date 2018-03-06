
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

**输入：** n位二进制整数A、B<br>
**输出：** n+1位的二进制整数C，C等于A、B之和


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

<center>3,41,52,26,38,57,9,49</center>
<center>|</center>
<center>(3,41),(26,52),(38,57)(9,49)</center>
<center>|</center>
<center>(3,26,41,52),(9,38,49,57)</center>
<center>|</center>
<center>(3,9,26,38,41,49,52,57)</center>

#### 2.3-2&ensp;不使用哨兵的merge_sort


```python
def merge_sort_noguard(A,p,r):
    if p < r:
        q = int(0.5*(p + r))
        merge_sort_noguard(A,p,q)
        merge_sort_noguard(A,q+1,r)
        return merge_noguard(A,p,q,r)

def merge_noguard(A,p,q,r):
    L, R = [], []
    for i in range(p,q+1):
        L.append(A[i])

    for j in range(q+1,r):
        R.append(A[j])

    i, j = 0, 0
    for k in range(p,r):
        if i == len(L):
            A[k] = R[j]
            j += 1
        elif j == len(R):
            A[k] = L[i]
            i += 1
        elif L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

    return A
```


```python
A = [4,9,78,99,100,65,97,237]
merge_sort_noguard(A,0,len(A))
```




    [4, 9, 65, 78, 97, 99, 100, 237]



#### 2.3-3&ensp;证明$T(n)=n\lg n$

1. 当n=2时，$T(n) = nlgn = 2\lg2 = 2*1 = 2$<br>
2. 当$n=2^k,k>1$时，$2T(n/2)+n=2[\frac{2^{k}}{2}*\lg\frac{2^{k}}{2})+2^{k}$=$2((k-1)*2^{k-1})+2^{k}=k2^{k}=n\lg{n} =T(n)$


#### 2.3-4&ensp;为插入排序的最坏情况运行时间写一个递归式

最坏情况：逆序<br>
运行时间：$T(n)=\begin{cases}
0，若n=1\\
T(n-1) + n-1，若n>1\\
\end{cases}$

#### 2.3-5&ensp;二分查找


```python
def binary_search(A,p,q,v):
    m = int(0.5*(p + q))
    if p+1 >= q:
        return "NIL"
    elif v == A[m]:
        return m
    elif v > A[m]:
        return binary_search(A,m,q,v)
    elif v < A[m]:
        return binary_search(A,p,m,v)
    else:
        return "NIL"

if __name__ == '__main__':
    A = [1,7,12,15,16,19]
    v = 2
    p = 0
    q = len(A)
    print(binary_search(A,p,q,v))
```

    NIL



```python
def binary_search(A,v):
    lower = 0
    high = len(A)
    while lower < high:
        m = int((lower + high)*0.5)
        if v == A[m]:
            return m
        elif v > A[m]:
            lower = m +1
        elif v < A[m]:
            high = m-1
    else:
        return "NIL"

if __name__ == '__main__':
    A = [1,7,12,15,16,19]
    v = 20
    p = 0
    q = len(A)
    print(binary_search(A,v))
```

#### 2.3-7&ensp;描述一个算法，使其在数组中找到两数之和为x，这个算法的运行时间为$\Theta(nlgn )$

1. 依次取出数组左边的元素key，这一步循环n次
2. 然后在右边剩余元素中查找x-key，使用二分查找最差情况（找不到）需要运行$(n-1)*lg(n-1)$
3. 总运行时间为$\begin{equation*}\sum\limits_{i=2}^{n}[(i-1)lg(i-1)]\end{equation*}$
4. 根据$\Theta($$\begin{equation*}\sum\limits_{k=1}^{n}f(k)\end{equation*}$$)=$$\begin{equation*}\sum\limits_{k=1}^{n}\Theta (f(k))\end{equation*}$，则总运行时间为$\Theta(nlgn)$

### 2.3&ensp;思考题

#### 2-1&ensp;在归并排序中对小数组采用插入排序

a.&ensp;最坏情况时完成$\frac{n}{k}$个长度为k的子表用时为$\frac{n}{k}*\Theta(k^{2})=\Theta(nk)$<br>
b.&ensp;在最坏情况下合并2个k子表，将其变成一个2k子表，用时:$\Theta(2k)$，有$\frac{n}{k}$个k子表需要合并，用时$\frac{n}{2k}*\Theta(2k)=\Theta(n)$<br>
&ensp;&ensp;&ensp;&ensp;k+k→2k，2k+2k→4k……$\frac{n}{2}+\frac{n}{2}→n$，这样的过程发生的次数是：$lg\frac{n}{k}$，所以运行时间为：$\Theta(n)*lg\frac{n}{k}=\Theta(nlg\frac{n}{k})$<br>
c.&ensp;**n最大值是：**2<br>
&ensp;&ensp;&ensp;要使$\Theta(nk+nlg\frac{n}{k})=\Theta(nlgn)$成立，使$k-lgk$最小,
d.&ensp;

#### 2-2&ensp;冒泡排序

a. 不需要了<br>
b. **循环不变式是：**在1……i处存放着序列中的较小值，并且已排好序<br>
c. **终止条件是：**i=A.length<br>
d. **最坏情况是：**逆序，运行时间是：$\begin{equation*}
\sum\limits_{i=1}^{n-1}\end{equation*}($
$\begin{equation*}
\sum\limits_{j=i+1}^{n} 2
\end{equation*})$=$\Theta(n^{3})$

#### 2-3&ensp;霍纳规则的正确性

a.&ensp;$\Theta(n)$<br>
b.&ensp;需要运行cn次，和霍纳规则相比，性能相同


```python
def polynomial_evaluation(A,x):
    return A[0] * x**0 + A[1] * x**1 + A[2] * x**2

A = [1,2,4]
x = 3
polynomial_evaluation(A,x)
```




    43



c.&ensp;循环终止时i=-1，带入后可得$y=\begin{equation*}\sum\limits_{k=0}^{n}a_{k}x^{k}\end{equation*}$<br>
d.&ensp;循环不变式：y是正确的多项式，每循环一次，传入新值$a_i$，并且将y乘以x

#### 2-4&ensp;逆序对

a.&ensp;(0,4),(1,4),(2,3),(2,4),(3,4)<br>
b.&ensp; **最多逆序对：**为逆序集合时，逆序对数量为：$num = \begin{equation*}\sum\limits_{i=1}^{n-1}n-i\end{equation*}=\frac{1}{2}n(n-1)$<br>
c.&ensp;T(n) = c\*num,c为常数<br>
d.&ensp;确定逆序对数量的算法，运行时间为：$\Theta(n^2)$


```python
def inversion(A):
    num = 0
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            if A[i] > A[j]:
                num += 1
    return num

A = [2,3,8,6,1]
inversion(A)
```




    5



&ensp;&ensp;运行时间为：$\Theta(nlgn)$


```python

```
